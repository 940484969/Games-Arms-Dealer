from django.contrib import admin
from django.urls import path, include, re_path
from app_cart.views import *

urlpatterns = [
    # re_path('cart/', CartView.as_view(), name='cart'),
    re_path('cart_page/', CartPageShow.as_view(), name='cart_page'),
    re_path('add_page/', AddPageCart.as_view(), name='add_page'),
    re_path('sub_page/', SubtractPageCart.as_view(), name='sub_page'),
    # re_path('add_num_cart/', AddNumCart.as_view(), name='add_num'),

]
