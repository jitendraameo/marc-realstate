from django.shortcuts import render
from django.http import request


def home(request):
    return render(request, 'buyer/index.html')   


def advance_search(request):
    return render(request, 'buyer/advance-search.html')  


def foreclosure_search(request):
    return render(request, 'buyer/foreclosure.html')  


def blog_search(request):
    return render(request, 'buyer/blog.html')  


def about_view(request):
    return render(request, 'buyer/aboutus.html')  
        

def contact_view(request):
    return render(request, 'buyer/contact.html')


def market_view(request):
    return render(request, 'buyer/advance-search.html')

def property_search_view(request):

    return render(request, 'buyer/property.html')


