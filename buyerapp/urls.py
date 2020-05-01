from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('advance_search', advance_search),
]
