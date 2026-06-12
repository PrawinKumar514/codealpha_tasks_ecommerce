# ecommerce/store/urls.py

from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path(
        'products/',
        views.ProductListView.as_view(),
        name='product_list'
    ),

    path(
        'products/category/<slug:category_slug>/',
        views.ProductListView.as_view(),
        name='product_list_by_category'
    ),

    path(
        'product/<slug:slug>/',
        views.ProductDetailView.as_view(),
        name='product_detail'
    ),

    # Cart
    path(
        'cart/',
        views.cart_view,
        name='cart'
    ),

    path(
        'cart/add/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/update/',
        views.update_cart_item,
        name='update_cart'
    ),

    # Checkout
    path(
        'checkout/',
        views.checkout_view,
        name='checkout'
    ),

    # Orders
    path(
        'orders/',
        views.order_history,
        name='order_history'
    ),

    path(
        'order/<int:order_id>/',
        views.order_detail,
        name='order_detail'
    ),

    path(
        'order/<int:order_id>/cancel/',
        views.cancel_order,
        name='cancel_order'
    ),

    path(
        'order/<int:order_id>/delete/',
        views.delete_order,
        name='delete_order'
    ),

    # Profile
    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    # Register
    path(
        'register/',
        views.register,
        name='register'
    ),
]