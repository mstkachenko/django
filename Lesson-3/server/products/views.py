import json
from django.urls import reverse
from django.shortcuts import render

from .models import Product

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