from django.urls import path
from .views import (
    contacts,catalog,main,about)


#app_name='main'

urlpatterns = [
path('',main, name='main'),
path('contacts/',contacts, name='contacts'),
path('about/',about, name='about'),

]