from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product, Supplier, Stock

@receiver(post_save, sender=Product)
def update_product_count_on_create(sender, instance, created, **kwargs):
    if created:
        supplier = instance.supplier
        supplier.product_count = Product.objects.filter(supplier=supplier).count()
        supplier.save()

@receiver(post_delete, sender=Product)
def update_product_count_on_delete(sender, instance, **kwargs):
    supplier = instance.supplier
    supplier.product_count = Product.objects.filter(supplier=supplier).count()
    supplier.save()

@receiver(post_save, sender=Product)
def create_stock_for_new_product(sender, instance, created, **kwargs):
    if created:
        Stock.objects.create(
            supplier=instance.supplier,
            product=instance,
            quantity=0
        )