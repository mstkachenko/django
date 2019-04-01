import json
from django.urls import reverse
from django.shortcuts import render, redirect

from .models import Product, ProductCategory
from .forms import ProductCategoryForm, ProductCategoryModelForm

# Create your views here.

def product_list(request):
    #with open('products/fixtures/data/data.json') as file:
    #    return render(
    #        request,
    #        'products/catalog.html',
    #        {'object_list': json.load(file)}
    #    )
    return render(
        request,
        'products/catalog.html',
        {'object_list':Product.objects.all()}
    )

def product_detail(request, pk):
    #with open('products/fixtures/data/data.json') as file:
    #    return render(
    #        request,
    #        'products/detail.html',
    #        {'object':json.load(file)[pk]}
    #    )
    return render(
        request,
        'products/detail.html',
        {'object':Product.objects.get(id=pk)}
    )

def category_create(request):
    form = ProductCategoryModelForm()
    if request.method == 'POST':
        form = ProductCategoryModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            #ProductCategory.objects.create(
            #    name = form.cleaned_data.get('name')    
            #)
            return redirect('products:main')

    return render(
        request,
        'categories/create.html',
        {'form':form}
    )