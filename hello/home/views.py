from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, contactno=contactno, message=message)
        contact.save()
        messages.success(request, 'Your Message Send')
        
    context = {
        'Variable': 'This is a variable'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def supportus(request):
    return render(request, 'supportus.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, contactno=contactno, message=message)
        contact.save()
        messages.success(request, 'Your Message Send')
    return render(request, 'contact.html')