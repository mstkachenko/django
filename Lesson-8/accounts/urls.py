from django.urls import path
from django.contrib.auth.views import (
    LoginView
)

from .views import (
    login_view,AccountLoginView,AccountRegistrationView,
    AccountLogoutView
)


app_name = 'accounts'

urlpatterns = [
    path('', AccountLoginView.as_view(), name='login'),
    path('registration/',AccountRegistrationView.as_view(),name='registration'),
    path('logout/',AccountLogoutView.as_view(),name='logout'),
]