from django.contrib import admin
from django.urls import path, include, re_path
from app_commidity.views import *

urlpatterns = [
    re_path('index/', IndexShow.as_view(), name='index'),
    re_path('product/', ProductShow.as_view(), name='product'),
    re_path('category/', Category.as_view(), name='category'),
    re_path('category/action/', Category.as_view(), name='action'),
    # re_path(r"['category/(?P<action>[^/]+)/\\Z']", Category.as_view(), name='action'),
    re_path(r'category/venture/', Category.as_view(), name='venture'),
    re_path(r'category/single/', Category.as_view(), name='single'),
    re_path(r'category/multiplayer/', Category.as_view(), name='multiplayer'),
    re_path(r'category/drama/', Category.as_view(), name='drama'),
    re_path(r'category/sports/', Category.as_view(), name='sports'),
    re_path(r'category/horror/', Category.as_view(), name='horror'),

    # Action
# Venture
# Single
# Multiplayer
# Drama
# Sports
# Horror
]
