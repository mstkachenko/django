from django.urls import path

from products.views import (
    product_list, product_detail, product_create, 
    product_delete, product_rest_list,
    ProductCreate, ProductUpdate,ProductDelete,
    ProductList,ProductDetail
    #product_update
)


app_name = 'products'

urlpatterns = [
	path('create/', ProductDelete.as_view(), name='create'),
    path('<int:pk>/update/',ProductUpdate.as_view(), name='update'),
    path('<int:pk>/delete/',ProductDelete.as_view(), name='delete'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='main'),
]

urlpatterns += [
    path('api/', product_rest_list, name='rest_list')
]