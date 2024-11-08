# your_app/context_processors.py
from .models import Supplier

def suppliers(request):
    return {
        'suppliers': Supplier.objects.all()
    }
