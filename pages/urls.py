from django.contrib import admin
from django.urls import path
from . import views

import pages

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
