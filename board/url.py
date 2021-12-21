from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from board import views

urlpatterns = [
    path(r'', views.board),
    path(r'find', views.find),
]