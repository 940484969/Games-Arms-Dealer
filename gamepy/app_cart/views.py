from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.views import View
# Create your views here.
from app_commidity.models import *
from app_cart.models import *

from redis import StrictRedis

from app_user.models import User

from django.core import serializers





class CartPageShow(View):
    """
    购物车展示界面
    """

    def get(self, request):
        """

        :param request:
        :return:
            game_kind_num :
                该用户的订单内容  为多对多 订单中的游戏 [（是什么，有几个）即SkuNum] 的queryset对象
        """
        cart_name = []

        user_cart = CartItem.objects.filter(user_id=request.user.id, cart_is_del=0).first()
        # print(user_cart)

        # game_name = user_cart.sku_id.all().values_list('sku_name')
        try:
            game_kind_num = user_cart.sku_id.filter(cartitem__cart_is_del=0)
            # print(game_kind_num)
            sum_cart_price = 0
            for i in game_kind_num:
                sum_cart_price += i.num * i.sku_id.sku_price
                discout_price = sum_cart_price * i.sku_id.sku_discount
            sum_cart_price = round(sum_cart_price, 2)
            discout_price = round(discout_price, 2)
            save_price = round(sum_cart_price - discout_price, 2)
        except Exception:
            pass
        return render(request, 'cart.html', locals())


# class CartPageShow(View):
#     """
#     购物车展示界面
#     """
#
#     def get(self, request):
#         """
#
#         :param request:
#         :return:
#             game_kind_num :  <QuerySet [<SkuNum: SkuNum object (1)>, <SkuNum: SkuNum object (2)>]>
#                 该用户的订单内容  为多对多 订单中的游戏 [（是什么，有几个）即SkuNum] 的queryset对象
#         """
#         cart_name = []
#
#         user_cart = CartItem.objects.filter(user_id=request.user.id).first()
#         # print(user_cart)
#
#         # game_name = user_cart.sku_id.all().values_list('sku_name')
#         game_kind_num = user_cart.sku_id.all()
#
#         # print(game_kind_num)
#         sum_cart_price = 0
#         for i in game_kind_num:
#             sum_cart_price += i.num * i.sku_id.sku_price
#             discout_price = sum_cart_price * i.sku_id.sku_discount
#
#         save_price = sum_cart_price - discout_price
#
#         return render(request, 'cart.html', locals())


class AddPageCart(View):
    """
    购物车界面内的加
    """

    def post(self, request):
        obj_id = int(request.POST.get('obj_id'))
        obj = SkuNum.objects.filter(num_id=obj_id).first()
        # print(obj)
        obj.num += 1
        obj.save()
        # print(obj.num)
        user_cart = CartItem.objects.filter(user_id=request.user.id, cart_is_del=0).first()
        # print(user_cart)
        game_kind_num = user_cart.sku_id.filter(cartitem__cart_is_del=0)
        sum_cart_price = 0
        for i in game_kind_num:
            sum_cart_price += i.num * i.sku_id.sku_price
            discout_price = sum_cart_price * i.sku_id.sku_discount

        sum_cart_price = round(sum_cart_price, 2)
        discout_price = round(discout_price, 2)
        save_price = round(sum_cart_price - discout_price, 2)

        response = JsonResponse({"obj_num": obj.num, "sum_cart_price": sum_cart_price,
                                 "discout_price": discout_price, "save_price": save_price})

        return response

    def get(self, request):
        if not request.user.is_authenticated:
            cart_num = 0
            response = JsonResponse({'cart_num': cart_num})
            return response


        """
        该函数为get方法  即 主页页面分类中的购物车按钮
        :param request:
        :return:
        """
        user = request.user
        # 前端传递 sku的id
        id_sku = request.GET.get("sku_id")
        # 获取当前用户的购物车表
        cart_user = CartItem.objects.filter(user_id__id=user.id, cart_is_del=0).first()

        try:
            if not cart_user:
                # 不存在 则创建     增加sku的数量表信息  增加购物车表信息  建立多对多关系
                obj = SkuNum.objects.create(num=1, sku_id_id=id_sku)
                print(1111)
                user_shopping = CartItem.objects.create(cart_is_del=0, cart_count=0, user_id=user)
                user_shopping.sku_id.add(obj)
                user_shopping.save()
                cart_num = 1
            else:
                # 存在 选择 该用户的购物车信息
                user_shopping_sku = CartItem.objects.filter(cart_is_del=0, user_id=user).first()
                if user_shopping_sku:
                    cls_num = user_shopping_sku.sku_id.filter(sku_id=id_sku, cartitem__cart_is_del=0).first()
                    if cls_num:
                        # 如果该sku的id 在购物车中  数量+=1
                        cls_num.num += 1
                        cls_num.save()

                    else:
                        # 不在  则创建 sku数量信息 （该sku 的id和数量）

                        k = SkuNum.objects.create(sku_id_id=id_sku, num=1)
                        cls_num = user_shopping_sku.sku_id.add(k)
                        # cls_num.save()

                all_num = user_shopping_sku.sku_id.filter(cartitem__cart_is_del=0)

                cart_num = 0

                for i in all_num:
                    cart_num += i.num
        except Exception:
            cart_num = 0


        # return response_success(message='后台响应成功', data_list=serializers.serialize("json", books))
        response = JsonResponse({'cart_num': cart_num})
        return response


# class AddNumCart(View):
#     def post(self, request):
#         """
#         该函数为get方法  即 主页页面分类中的购物车按钮
#         :param request:
#         :return:
#         """
#         print(1111)
#         # print(request.GET.get("k"))
#         a = 123
#         response = JsonResponse(locals())
#         return response


class SubtractPageCart(View):
    """
    购物车界面  商品减少一个 最小为1
    """

    def post(self, request):
        obj_id = int(request.POST.get('obj_id'))
        # print(obj_id)
        obj = SkuNum.objects.filter(num_id=obj_id).first()
        if obj.num > 1:
            # print(obj)
            obj.num -= 1
            obj.save()
            # print(obj.num)

        else:
            pass

        user_cart = CartItem.objects.filter(user_id=request.user.id, cart_is_del=0).first()
        # print(user_cart)
        game_kind_num = user_cart.sku_id.filter(cartitem__cart_is_del=0)
        sum_cart_price = 0
        for i in game_kind_num:
            sum_cart_price += i.num * i.sku_id.sku_price
            discout_price = sum_cart_price * i.sku_id.sku_discount

        sum_cart_price = round(sum_cart_price, 2)
        discout_price = round(discout_price, 2)
        save_price = round(sum_cart_price - discout_price, 2)

        response = JsonResponse({"obj_num": obj.num, "sum_cart_price": sum_cart_price,
                                 "discout_price": discout_price, "save_price": save_price})
        return response
