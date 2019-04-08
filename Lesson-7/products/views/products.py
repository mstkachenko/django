import json
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.core.paginator import Paginator
from django.views.generic import(
    View,CreateView, UpdateView, 
    DeleteView, ListView,DetailView
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

class ProductCreate(CreateView):
    model = Product
    fields = (
            'name', 'image', 'category', 
            'description', 'cost'
    )
    template_name='products/create.html'
    success_url='products:main'
    
    # def get(self, *args, **kwargs):
    #     return render(
    #         self.request,
    #         self.template_name,
    #         {'form':self.form_class()}
    #     )

    # def post(self, *args, **kwargs):
    #     form = self.form_class(
    #         data=self.request.POST,
    #         files=self.request.FILES
    #     )

    #     if form.is_valid():
    #         form.save()
    #         return redirect(self.success_url)

    #     return render(
    #         self.request,
    #         self.template_name,
    #         {'form':self.form_class()}
    #     )
        
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

class ProductUpdate(UpdateView):
    model = Product
    form_class=ProductForm
    template_name='products/update.html'
    success_url='products:main'

# def product_update(request, pk):
#     obj = get_object_or_404(Product, pk=pk)

#     form = ProductForm(
#         instance=obj
#     )

#     if request.method == 'POST':
#         form = ProductForm(
#             request.POST,
#             files=request.FILES,
#             instance=obj,
#         )

#         if form.is_valid():
#             form.save()

#             return redirect('products:main')

#     return render(
#         request,
#         'categories/update.html',
#         {'form': form}
#     )

class ProductDelete(DeleteView):
    model = Product
    form_class=ProductForm
    template_name='products/delete.html'


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

class ProductList(ListView):
    model = Product
    template_name='products/catalog.html'
    paginate_by=3


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
class ProductDetail(DetailView):
    model = Product
    template_name='products/detail.html'

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
