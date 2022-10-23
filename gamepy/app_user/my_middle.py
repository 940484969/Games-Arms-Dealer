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
        elif request.path.startswith('/change/'):
            pass
        elif not request.user.is_authenticated:
            return redirect('%s?next=%s' % (LOGIN_URL, request.path), locals())
        else:
            pass

    def process_response(self, request, response):
        cate_kind = CommodityKind.objects.all()
        # print('lhd')
        response["cate_kind"] = cate_kind
        # response['songheizi'] = request.user.is_authenticated
        # print(request.user)
        if request.user.is_authenticated:
            # print(1111)
            try:
                all_num = CartItem.objects.filter(user_id=request.user, cartitem__cart_is_del=0).first().sku_id.all()
                cart_num = 0
                if all_num:
                    for i in all_num:
                        cart_num += i.num
            except:
                cart_num = 0
            response['cart_num'] = cart_num
        # print(response['a'])
        # print(response["user"].is_authenticated())
        # return HttpResponse(response)
        return response
