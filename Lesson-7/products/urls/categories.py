from django.urls import path

from products.views import (
    category_create, category_update, category_delete,
	category_detail, category_list, CategoryCreate,
    CategoryUpdate, CategoryDelete, CategoryDetail,
    CategoryList
)


app_name = 'categories'

urlpatterns = [
    path('create/', CategoryCreate.as_view(), name='create'),
    path('<int:pk>/update/', CategoryUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', CategoryDelete.as_view(), name='delete'),
	path('<int:pk>/', CategoryDetail.as_view(), name='detail'),
    path('', CategoryList.as_view(), name='main'),
]
