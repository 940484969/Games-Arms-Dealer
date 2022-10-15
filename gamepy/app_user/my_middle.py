from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from .views import *

from gamepy.settings import LOGIN_URL


class CustomAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/login/'):
            pass
        elif request.path.startswith('/register/'):
            pass
        elif request.path.startswith('/index/'):
            pass
        elif request.path.startswith('/admin/'):
            pass
        elif not request.user.is_authenticated:
            return redirect('%s?next=%s' % (LOGIN_URL, request.path))
        else:
            pass
