from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main/index.html')

def phone(request):
    return render(request, 'main/phone.html')

def contacts(request):
    return render(request, 'main/contacts.html')