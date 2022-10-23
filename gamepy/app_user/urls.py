from django.contrib import admin
from django.urls import path, include, re_path
from app_user.views import *
from django.urls import reverse
urlpatterns = [
    re_path('login/', Login.as_view(), name='login'),
    re_path('register/', Register.as_view(), name='register'),
    re_path('xieyi/', XieyiShow.as_view(), name='xieyi'),
    re_path('change/', ChangePasswd.as_view(), name='change'),
    re_path('my_index/', MyIndexPasswd.as_view(), name='my_index'),
    re_path('logout/', Logout.as_view(), name='logout'),
]
