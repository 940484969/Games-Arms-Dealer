import re

from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.views import View
# from django.contrib.auth.models import User
from app_user.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "account.html")

    def post(self, request):
        username = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse('666')
        return redirect(reverse('index'))


class XieyiShow(View):
    def get(self, request):
        return render(request, "xieyi.html")


class Register(View):
    def get(self, request):
        return render(request, "registered.html")

    def post(self, request):

        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        # phone = request.POST['phone']
        # gender = request.POST['gender']
        password = request.POST['password']
        try:
            is_exists = User.objects.get(username=username)
        except Exception:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                            last_name=lastname, is_staff=1)
            return redirect(reverse('account'))

        # if not re.match(r'^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$', email):
        #     return render(request, 'index.html', {'errmsg': '邮箱不符合规范'})

        return render(request, "registered.html")
