from django.contrib import admin
from django.urls import path, include, re_path
from app_user.views import *
from django.urls import reverse
urlpatterns = [
    re_path('user/', Login.as_view(), name='account'),
    re_path('register/', Register.as_view(), name='register'),
    re_path('xieyi/', XieyiShow.as_view(), name='xieyi'),
]
