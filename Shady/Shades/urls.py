from django.urls import path
from .import views

urlpatterns =[
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('womenseyeglasses', views.womenseyeglasses, name='womenseyeglassses'),
    path('menseyeglasses', views.menseyeglasses, name='menseyeglassses'),
    path('item', views.item, name='item'),
    path('carts', views.cart, name='cart'),
    path('checkout', views.checkout, name="checkout")
]