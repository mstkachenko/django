from django.urls import path

from products.views import (
    category_create, category_update, category_delete,
	category_detail, category_list
)


app_name = 'categories'

urlpatterns = [
    path('create/', category_create, name='create'),
    path('<int:pk>/update/', category_update, name='update'),
    path('<int:pk>/delete/', category_delete, name='delete'),
	path('<int:pk>', category_detail, name='detail'),
    path('', category_list, name='main'),
]
