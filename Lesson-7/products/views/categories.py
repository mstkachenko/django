from django.urls import reverse
from django.shortcuts import (
    render, redirect, get_object_or_404
)

from django.core.paginator import Paginator
from django.views.generic import(
    CreateView, UpdateView, 
    DeleteView, ListView,DetailView
)

from products.models import Category
from products.forms import CategoryForm, CategoryModelForm

class CategoryCreate(CreateView):
    model = Category
    form_class=CategoryModelForm
    template_name='categories/create.html'
    success_url='products:main'

class CategoryUpdate(UpdateView):
    model = Category
    form_class=CategoryModelForm
    template_name='categories/update.html'
    success_url='products:main'

class CategoryDelete(DeleteView):
    model = Category
    form_class=CategoryModelForm
    template_name='categories/delete.html'

class CategoryList(ListView):
    model = Category
    template_name='categories/index.html'

class CategoryDetail(DetailView):
    model = Category
    template_name='categories/detail.html'

    def get_context_data(self, *args, **kwargs):
        obj = kwargs.get('object')
        print(kwargs)
        page_num = self.request.GET.get('page')
        paginator = Paginator(obj.product_set.all(),1)
        paginator.get_page(page_num)
        return {
            'object':obj,
            'page_object':paginator.get_page(page_num)
        }

def category_create(request):
    form = CategoryModelForm()
    if request.method == 'POST':
        form = CategoryModelForm(
            data=request.POST,
            files=request.FILES,
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

	
def category_list(request):
    return render(
        request,
        'categories/index.html',
        {'object_list': Category.objects.all()}
    )


def category_detail(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    return render(
        request,
        'categories/detail.html',
        {'object': obj}
    )

