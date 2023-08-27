from django.shortcuts import render

def home(request):
    return render(request, 'it_landing/home.html')

def about(request):
    return render(request, 'it_landing/about.html')

def services(request):
    return render(request, 'it_landing/services.html')

def contact(request):
    return render(request, 'it_landing/contact.html')