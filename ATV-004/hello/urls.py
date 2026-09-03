from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('', views.HelloView.as_view(), name='HelloView'),
]
