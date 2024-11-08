from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Supplier, Product, Stock
from .forms import Supplierform, Productform, StockForm
from django.contrib.auth.decorators import login_required

def home(request):
    suppliers = Supplier.objects.all()
    products = Product.objects.all()
    stocks = Stock.objects.all()


    return render(request, 'home.html', {
        'suppliers': suppliers,
        'products': products,
        'stocks': stocks,
    })

def view_products(request, supplier_id):
    products = Product.objects.filter(supplier_id=supplier_id).order_by('-date')
    supplier = Supplier.objects.get(id=supplier_id)
    stocks = Stock.objects.all()
    
    return render(request, "products.html", {"products": products, 'supplier': supplier, "stocks": stocks})

def add_supplier(request):
    if request.method == "POST":
        form = Supplierform(request.POST)
        if form.is_valid:
            Supplier = form.save(commit=False)
            Supplier.user = request.user
            Supplier.save()
            messages.success(request, "Supplier was successfully added")
            return redirect("home")
        else:
            messages.warning(request, 'Something went wrong. Please try again.')
    else :
        form = Supplierform()
    return render(request, "add_supplier.html", { "form" : form })

def add_products(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    if request.method == "POST":
        form = Productform(request.POST)
        if form.is_valid:
            product = form.save(commit=False)
            product.supplier = supplier
            product.save()
            messages.success(request, "Product was successfully added")
            return redirect("view_products", supplier_id=supplier.id)
        else:
            messages.warning(request, 'Something went wrong. Please try again.')
    else:
        form = Productform()
    return render(request, "add_products.html", {"supplier": supplier, 'form': form})

@login_required
def delete_supplier(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    if supplier and request.user == supplier.user:
        supplier.delete()
        return redirect('home')
    else :
        messages.success(request, "You are not eligible to delete this supplier")
        return redirect("home")

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user == product.supplier.user:
        product.delete()
        messages.success(request, "Product was deleted.")
        return redirect("view_products", supplier_id=product.supplier.id)
    else:
        messages.error(request, "You are not the owner of this product.")
        return redirect("view_products", supplier_id=product.supplier.id)

def update_stocks(request, stock_id):
    stock = Stock.objects.get(id=stock_id)
    product = Product.objects.get(name=stock.product)
    supplier = Supplier.objects.get(name=product.supplier)

    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid:
            form.save()
            messages.success(request, "Your sock was updated")
            return redirect( "view_products", supplier_id= supplier.id)
        else :
            messages.error(request, "something went wrong")
    else :
        form = StockForm(instance=stock)
    return render(request, "update_stock.html", {'stock' : stock, 'product' : product, "form" : form})

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    supplier = product.supplier 

    if request.method == "POST":
        form = Productform(request.POST, instance=product)
        if form.is_valid:
            form.save()
            messages.success(request, "Your Product was updated")
            return redirect( "view_products", supplier_id= supplier.id)
        else :
            messages.error(request, "something went wrong")
    else :
        form = Productform(instance=product)
    return render(request, "update_product.html", {"form": form, "supplier" : supplier, "product" : product })