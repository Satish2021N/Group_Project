from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id=models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
class Mens_Eye_Glasses(models.Model):
    name=models.CharField(max_length=200, null=True)
    price=models.IntegerField()
    image=models.ImageField(null=True, blank=True)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Womens_Eye_Glasses(models.Model):
    name=models.CharField(max_length=200, null=True)
    price=models.IntegerField()
    image=models.ImageField(null=True, blank=True)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Mens_Sun_Glasses(models.Model):
    name=models.CharField(max_length=200, null=True)
    price=models.IntegerField()
    image=models.ImageField(null=True, blank=True)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Womens_Sun_Glasses(models.Model):
    name=models.CharField(max_length=200, null=True)
    price=models.IntegerField()
    image=models.ImageField(null=True, blank=True)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Blue_Ray_Glasses(models.Model):
    name=models.CharField(max_length=200, null=True)
    price=models.IntegerField()
    image=models.ImageField(null=True, blank=True)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    product = models.ForeignKey(Mens_Eye_Glasses, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_orderd = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address=models.CharField(max_length=200, null=True)
    city=models.CharField(max_length=200, null=True)
    state=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.address
        
