from django.contrib import admin
from django.urls import path, include, re_path
from app_commidity.views import *

urlpatterns = [
    re_path('index/', IndexShow.as_view(), name='index')
]
