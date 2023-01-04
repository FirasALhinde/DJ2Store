from django.shortcuts import render,get_object_or_404   
from .models import Product
# Create your views here.

def product_list(request):
    all_product = Product.objects.all()
    return render(request,'products/product_list.html',{'all_product':all_product})

def product_detail(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'products/product_detail.html',{'product':product})