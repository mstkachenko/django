from django.urls import path

from products.views import (
    product_list, product_detail, product_create, 
    product_update, product_delete, product_rest_list
)


app_name = 'products'

urlpatterns = [
	path('create/', product_create, name='create'),
    path('<int:pk>/update/', product_update, name='update'),
    path('<int:pk>/delete/', product_delete, name='delete'),
    path('<int:pk>/', product_detail, name='detail'),
    path('', product_list, name='main'),
]

urlpatterns += [
    path('api/', product_rest_list, name='rest_list')
]