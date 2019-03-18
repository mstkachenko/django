from django.shortcuts import render

# Create your views here.

def product_list(request):
    return render(request,'products/catalog.html')

def product_detail(request):
    return render(request,'products/detail.html')