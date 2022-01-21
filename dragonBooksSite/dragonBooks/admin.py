from django.contrib import admin
from .models import Products
# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)