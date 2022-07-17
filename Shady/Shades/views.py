from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from .models import *

# Create your views here.
def index(request):
    return render(request, 'Home/home.html')

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form":form})

def womenseyeglasses(request):
    return render(request, 'category/eyeglasses/Womens_Eye_Glasses.html')

def menseyeglasses(request):
    products = Mens_Eye_Glasses.objects.all()
    context = {'products':products}
    return render(request, 'category/eyeglasses/Mens_Eye_Glasses.html', context)

def item(request):
    return render(request, 'items/item.html')

def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    context = {'items':items}
    return render(request, 'items/cart.html',context)

def checkout(request):
    return render(request, 'items/checkout.html')
