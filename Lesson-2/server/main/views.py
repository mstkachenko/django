from django.template import Template, Context
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import timezone


# Create your views here.

def main(request):
    #template = Template(
    #    'Hello {{name}}'      
    #)
    #contex=Context({
    #'name': 'Anton'
    #})
    #return HttpResponse(
    #    template.render(contex)
    #    )
    return render(request, 'main/index.html')

def phone(request):
    return render(request, 'main/phone.html')

def about(request):
    
    template=get_template(
        'main/about.html'
    )
    return HttpResponse(
        template.render({
        'value': 'раздел в стадии разработки!',
          
        })
    )
    #return render(request, 'main/about.html')

def contacts(request):
    contacts = ['Contact1','Contact2','Contact3']
    return render(request, 
    'main/contacts.html',
    {'contacts':contacts}
    )