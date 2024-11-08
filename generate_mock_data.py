import os
import django
import random
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from main.models import Product, Supplier

# Initialize Faker
f = Faker()

supplier_ = Supplier.objects.get(name='zain')
# Generate product data
products = []
for _ in range(20):
    product = {
        "name": f.name(),
        "price": round(random.uniform(10.0, 100.0), 2),
        "size": random.randint(1, 100),
        "brand": f.company(),
        "description":f.sentence()
    }
    products.append(product)

# Insert generated data into the database
for product in products:
    Product.objects.create(
        supplier=supplier_,
        name=product["name"],
        price=product["price"],
        brand=product["brand"],
        size=product["size"],
        description=product['description']
    )
