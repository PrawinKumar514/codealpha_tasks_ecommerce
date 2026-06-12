# ecommerce/store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse
import json
from .models import Category, Product, Cart, CartItem, Order, OrderItem
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, CheckoutForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('store:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'store/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/order_history.html', {'orders': orders})

class HomeView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.all()[:8]
        context['categories'] = Category.objects.all()
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.all()
        # Search
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Category filter
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['selected_category'] = self.kwargs.get('category_slug', '')
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = int(data.get('quantity', 1))
        
        product = get_object_or_404(Product, id=product_id)
        
        # Check stock
        if product.stock < quantity:
            return JsonResponse({'error': 'Not enough stock available'}, status=400)
        
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )
        
        if not created:
            if cart_item.quantity + quantity > product.stock:
                return JsonResponse({'error': 'Not enough stock available'}, status=400)
            cart_item.quantity += quantity
            cart_item.save()
        
        return JsonResponse({
            'success': True,
            'message': f'{product.name} added to cart',
            'cart_count': cart.get_total_items()
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def update_cart_item(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        item_id = data.get('item_id')
        action = data.get('action')

        quantity = data.get('quantity')
        if quantity is not None:
            quantity = int(quantity)

        cart_item = get_object_or_404(
            CartItem,
            id=item_id,
            cart__user=request.user
        )

        if action == 'remove':
            cart_item.delete()

            cart = request.user.cart

            return JsonResponse({
                'success': True,
                'message': 'Item removed',
                'cart_count': cart.get_total_items(),
                'total_price': str(cart.get_total_price()),
                'cart_empty': cart.get_total_items() == 0
            })

        elif action == 'update':

            if quantity and quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()

                cart = request.user.cart

                return JsonResponse({
                    'success': True,
                    'message': 'Cart updated',
                    'cart_count': cart.get_total_items(),
                    'item_total': str(cart_item.get_total_price()),
                    'total_price': str(cart.get_total_price()),
                    'cart_empty': False
                })

        return JsonResponse({'error': 'Invalid action'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    if cart.get_total_items() == 0:
        messages.warning(request, 'Your cart is empty')
        return redirect('store:cart')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data['full_name'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                postal_code=form.cleaned_data['postal_code'],
                phone=form.cleaned_data['phone'],
                total_amount=cart.get_total_price(),
                status='pending'
            )

            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )

                product = cart_item.product
                product.stock -= cart_item.quantity
                product.save()

            cart.items.all().delete()

            messages.success(
                request,
                f'Order #{order.id} placed successfully!'
            )

            return redirect('store:order_history')

    else:
        initial_data = {}

        try:
            profile = request.user.profile

            initial_data = {
                'full_name': f"{request.user.first_name} {request.user.last_name}".strip(),
                'phone': profile.phone,
                'address': profile.address,
                'city': profile.city,
                'postal_code': profile.postal_code,
            }

        except Profile.DoesNotExist:
            pass

        form = CheckoutForm(initial=initial_data)

    return render(request, 'store/checkout.html', {
        'form': form,
        'cart': cart
    })

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_detail.html', {'order': order})

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    if request.method == 'POST' and order.status == 'pending':

        # restore stock
        for item in order.items.all():
            product = item.product
            product.stock += item.quantity
            product.save()

        order.status = 'cancelled'
        order.save()

        messages.success(request, "Order cancelled successfully")

    else:
        messages.error(
            request,
            "This order cannot be cancelled"
        )

    return redirect('store:order_detail', order_id=order.id)

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    if order.status == 'cancelled':
        order.delete()
        messages.success(
            request,
            "Order removed from history"
        )
    else:
        messages.error(
            request,
            "Only cancelled orders can be removed"
        )

    return redirect('store:order_history')