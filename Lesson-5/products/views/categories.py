from django.urls import reverse
from django.shortcuts import (
    render, redirect, get_object_or_404
)

from products.models import Category
from products.forms import CategoryForm, CategoryModelForm


def category_create(request):
    form = CategoryModelForm()
    if request.method == 'POST':
        form = CategoryModelForm(
            data=request.POST,
            files=request.FIELS
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


def category_update(request, pk):
    obj = get_object_or_404(Category, pk=pk)

    form = CategoryModelForm(
        instance=obj
    )

    if request.method == 'POST':
        form = CategoryModelForm(
            request.POST,
            files=request.FIELS,
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


def category_delete(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        obj.delete()

        return redirect('products:main')

    return render(
        request,
        'categories/delete.html',
        {'object': obj}
    )
