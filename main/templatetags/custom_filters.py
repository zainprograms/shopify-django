# main/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return ''

@register.filter
def filter_supplier(products, supplier_id):
    return products.filter(supplier__id=supplier_id)


@register.filter
def get_stock_quantity(product, stocks):
    for stock in stocks:
        if stock.product == product:
            return stock.quantity
    return 0