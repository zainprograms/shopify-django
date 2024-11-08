from django.db import models
from django.conf import settings
from django.utils import timezone

class Supplier(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255,)
    address = models.TextField(blank=True, null=True)  # Add address field
    website = models.URLField()  # Add website field
    phone_number = models.CharField(max_length=20, blank=True)  # Add phone number field
    email = models.EmailField()  # Add email field
    company_registration_number = models.CharField(max_length=100, blank=True)  # Add company registration number field

    logo = models.ImageField(upload_to='supplier_logos/', blank=True, null=True)  # Add logo field
    date_created = models.DateTimeField(auto_now_add=True)  # Add date created field
    product_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Stock(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='stocks')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ({self.supplier.name})'

class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=250)
    brand = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
