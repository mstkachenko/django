import json
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.http import JsonResponse
from products.models import Product
from products.forms import ProductForm


def product_rest_list(request):
    data = []
    object_list = Product.objects.all()

    for itm in object_list:
        data.append(
            {
                'id': itm.id,
                'name': itm.name,
                'image': itm.image.url if itm.image else None,
                'category': itm.category.name,
                'description': itm.description,
                'cost': itm.cost,
                'created': itm.created,
                'modified': itm.modified,
            }
        )

    return JsonResponse({'results': data})


def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(
            data=request.POST,
            files=request.FILES
        )
        if form.is_valid():
            form.save()
            # Category.objects.create(
            #     name=form.cleaned_data.get('name')
            # )
            return redirect('products:main')

    return render(
        request,
        'categories/create.html',
        {'form': form}
    )


def product_update(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    form = ProductForm(
        instance=obj
    )

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            files=request.FILES,
            instance=obj,
        )

        if form.is_valid():
            form.save()

            return redirect('products:main')

    return render(
        request,
        'categories/update.html',
        {'form': form}
    )


def product_delete(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        obj.delete()

        return redirect('products:main')

    return render(
        request,
        'categories/delete.html',
        {'object': obj}
    )


def product_list(request):
    # with open('products/fixtures/data/data.json') as file:
    #     return render(
    #         request, 
    #         'products/index.html',
    #         {'object_list': json.load(file)}
    #     )
    return render(
        request,
        'products/catalog.html',
        {'object_list': Product.objects.all()[:3]}
    )


def product_detail(request, pk):
    # with open('products/fixtures/data/data.json') as file:
    #     return render(
    #         request, 
    #         'products/detail.html',
    #         {'object': json.load(file)[pk]}
    #     )
    obj = get_object_or_404(Product, pk=pk)
    return render(
        request,
        'products/detail.html',
        {'object': obj}
    )
