from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# from .models import AccountUser

from .forms import LoginForm

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
