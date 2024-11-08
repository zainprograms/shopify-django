from django import forms
from django.forms import ModelForm
from .models import Supplier, Product, Stock

class Supplierform(forms.ModelForm):

  class Meta :
    model = Supplier
    fields = "name",  "email", "contact_info", "website", "address", "phone_number", "company_registration_number" 

    widgets = { 
          'name' : forms.TextInput(attrs={'class':'form-control', "placeholder": ""}),
          'email' : forms.EmailInput(attrs={'class':'form-control', "placeholder": ""}),
          'contact_info' : forms.TextInput(attrs={'class':'form-control', "placeholder": ""}),
          'website' : forms.TextInput(attrs={'class':'form-control', "placeholder": ""}),
          'address' : forms.TextInput(attrs={'class':'form-control', "placeholder": ""}),
          'phone_number' : forms.NumberInput(attrs={'class':'form-control', "placeholder": ""}),
          'company_registration_number' : forms.NumberInput(attrs={'class':'form-control', "placeholder": ""}),}

class Productform(forms.ModelForm):

  class Meta :
    model = Product
    fields = "name",  "size", "brand", "price", "category", "description"

    widgets = { 
          'name' : forms.TextInput(attrs={'class':'form-control', "placeholder": ""}),
          'size' : forms.TextInput(attrs={'class':'form-control', "placeholder": ""}),
          'brand' : forms.TextInput(attrs={'class':'form-control', "placeholder": ""}),
          'price' : forms.NumberInput(attrs={'class':'form-control', "placeholder": ""}),
          'category' : forms.TextInput(attrs={'class':'form-control', "placeholder": ""}),
          'description' : forms.Textarea(attrs={'class':'form-control', "placeholder": ""}),}

class StockForm(forms.ModelForm):

  class Meta :
    model = Stock
    fields = "quantity", "description"

    widgets = { 
          'quantity' : forms.TextInput(attrs={'class':'form-control', "placeholder": ""}),
          'description' : forms.Textarea(attrs={'class':'form-control', "placeholder": "Write the description here."}),}