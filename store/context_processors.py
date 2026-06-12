# ecommerce/store/context_processors.py
from .models import Category

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def cart_count(request):
    count = 0
    if request.user.is_authenticated:
        cart = getattr(request.user, 'cart', None)
        if cart:
            count = cart.get_total_items()
    return {
        'cart_count': count
    }