from django.urls import path
from .views import (
    contacts,phone,main,about)

urlpatterns = [
path('',main, name='main'),
#path('phone/',phone),
path('contacts/',contacts, name='contacts'),
path('about/',about, name='about')
]