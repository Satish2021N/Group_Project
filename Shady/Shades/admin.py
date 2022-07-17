from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Customer)
admin.site.register(Mens_Eye_Glasses)
admin.site.register(Womens_Eye_Glasses)
admin.site.register(Mens_Sun_Glasses)
admin.site.register(Womens_Sun_Glasses)
admin.site.register(Blue_Ray_Glasses)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

