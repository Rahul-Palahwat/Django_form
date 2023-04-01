from django.shortcuts import render, HttpResponse

from datetime import datetime

# import Contact instance to save data from the form
from home.models import Contact


# for messages
from django.contrib import messages

# render is to render a template , and HttpResponse to render string

# Create your views here.


def index(request):
    # to render a string we have used HttpResponse but ideally we will use templates
    # return HttpResponse("This is homepage")

    # context is a set of variable which we send into the templates , it's like a python dictionary
    # We will use context to fetch some data from models or other stuffs
    context = {
        'variable': "this is sent",
    }
    return render(request, 'index.html', context)


def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')


def services(request):
    # return HttpResponse("This is service page")
    return render(request, 'services.html')


def contact(request):
    # return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        query = request.POST.get('query')
        contact = Contact(name=name, email=email, phone=phone,
                          password=password, query=query, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request, 'contact.html')
