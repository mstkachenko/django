from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from .models import AccountUser
from django.views.generic import CreateView
from django.contrib.auth.views import (
    LoginView,LogoutView
)
from .models import AccountUser
from .forms import (
    LoginForm, RegistrationForm
)

class AccountLoginView(LoginView):
    template_name='accounts/login.html'

class AccountLogoutView(LogoutView):
    template_name='accounts/login.html'

class AccountRegistrationView(CreateView):
    model=AccountUser
    form_class=RegistrationForm
    template_name='accounts/registration.html'
    success_url=reverse_lazy('main:main')

def post(self, *args, **kwargs):
    response = super(AccountRegistrationView, self).post(*args,**kwargs)
    if self.object:
        login(self.request,self.object)
    return response

def login_view(request):
    form = LoginForm()
    
    if request.method =='POST':
        form=LoginForm(data=request.POST)

        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
    
            user = authenticate(
                username=username,
                password=password
            )
            # AccountUser.objects.get(url)

            if user and user.is_active:
                login(request, user)
                return redirect('main:main')
                

    return render (
        request,
        'accounts/login.html',
        {'form':form}
    )
