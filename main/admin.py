from django.contrib import admin
from .models import Supplier, Stock, Product
# Register your models here.

admin.site.register(Supplier)
admin.site.register(Stock)
admin.site.register(Product)