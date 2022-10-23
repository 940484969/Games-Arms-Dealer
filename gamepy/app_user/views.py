import re

from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.views import View
from django.contrib.auth import logout

from app_cart.models import CartItem
from app_commidity.models import CommodityKind
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
        # print(user)
        # print(type(user))
        if user is not None:
            login(request, user)
        else:
            messages.success(request, "密码错误")
            return render(request, "account.html", )
        return redirect(reverse('app_commidity:index'), locals())


class XieyiShow(View):
    def get(self, request):

        return render(request, "xieyi.html")

class Register(View):
    def get(self, request):
        # cate_kind = CommodityKind.objects.all()
        return render(request, "registered.html")

    def post(self, request):

        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        # gender = request.POST['gender']
        password = request.POST['password']
        try:
            is_exists = User.objects.get(username=username)
            messages.success(request, "用户名已被使用")
        except Exception:
            try:
                exists_phone = User.objects.get(phone=phone)
                messages.success(request, "您的手机号已被使用")
            except Exception:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                                phone=phone, last_name=lastname, is_staff=1)
                return redirect(reverse('app_user:login'))

        # if not re.match(r'^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$', email):
        #     return render(request, 'index.html', {'errmsg': '邮箱不符合规范'})

        return render(request, "registered.html")


from django.contrib import messages


class ChangePasswd(View):

    def get(self, request):

        return render(request, "change_passwd.html")

    def post(self, request):
        username = request.POST['username']
        web_phone = request.POST['phone']
        passwd = request.POST['password']

        try:

            data = User.objects.filter(username=username)[0]
            phone = data.phone
            if web_phone == phone:

                data.set_password(passwd)

                data.save()
                messages.error(request, "修改成功")

                return redirect(reverse('app_user:login'))
            else:
                messages.success(request, "请重新输入正确的手机号")
                # return redirect(reverse('account'))
                return render(request, "change_passwd.html")

        except Exception:

            messages.success(request, "请重新输入正确的用户")
            # return redirect(reverse('account'))
            return render(request, "change_passwd.html")

class  Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('app_user:login'))







# 设置全局参数
def global_params(request):
    cate_kind = CommodityKind.objects.all()
    if request.user.is_authenticated:
        try:
            all_num = CartItem.objects.filter(user_id=request.user, cart_is_del=0).first().sku_id.all()

            cart_num = 0
            for i in all_num:
                cart_num += i.num
        except Exception:
            cart_num = 0
    return locals()




class MyIndexPasswd(View):
    def get(self, request):
        user = request.user
        return render(request, 'my_index.html', locals())