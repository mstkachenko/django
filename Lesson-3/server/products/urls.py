from django.urls import path, re_path
from .views import( 
    product_list,product_detail)

from django.conf import settings
from django.conf.urls.static import static

app_name='products'

urlpatterns = [
path('', product_list,name='main'),
path('<int:pk>/',product_detail,name='detail') #- 1 вариант
#re_path(r'/',product_detail,name='detail')]  - 2 вариант
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)