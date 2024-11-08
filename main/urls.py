from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('view_products/<int:supplier_id>', views.view_products , name="view_products"),
    path('add_supplier', views.add_supplier , name="add_supplier"),
    path('add_products/<int:supplier_id>', views.add_products , name="add_products"),
    path('delete_supplier/<int:supplier_id>', views.delete_supplier , name="delete_supplier"),
    path('delete_product/<int:product_id>', views.delete_product , name="delete_product"),
    path('update_stock/<int:stock_id>', views.update_stocks , name="update_stock"),
    path('update_product/<int:product_id>', views.update_product , name="update_product")
]
