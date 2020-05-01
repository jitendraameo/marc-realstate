from django.shortcuts import render
from django.http import request


def home(request):
    return render(request, 'buyer/index.html')   

def advance_search(request):
    return render(request, 'buyer/advance-search.html')  