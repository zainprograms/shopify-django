# Generated by Django 5.0.6 on 2024-06-14 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_supplier_product_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='product_name',
            new_name='product',
        ),
    ]