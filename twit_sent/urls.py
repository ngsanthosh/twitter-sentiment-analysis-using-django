from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('external/', views.external, name='hello'),

    #path('', views.hello, name='hello'),
]
