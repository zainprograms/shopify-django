# Generated by Django 5.0.6 on 2024-06-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_supplier_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='company_registration_number',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact_info',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone_number',
            field=models.CharField(blank=True, default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='website',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
