from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

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
    return render(request, 'category/eyeglasses/Mens_Eye_Glasses.html')

def item(request):
    return render(request, 'items/item.html')