from django.contrib import admin
from django.urls import path, include
from online_bank import views

urlpatterns = [
   
    path("contact/", views.contact, name='contact'),
    path('index/',views.index, name='index'),
    path('home/',views.index, name='home'),
    path('display/',views.display, name='display'),
    path('deposit/',views.index, name='deposit'),
    path('transfer/',views.index, name='transfer'),
    path('withdraw/',views.index, name='withdraw'),
]
