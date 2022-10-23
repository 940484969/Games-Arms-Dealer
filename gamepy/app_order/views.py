import datetime

from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.views import View

from app_order.models import *
from app_cart.models import *





# Create your views here.

class OrderDetail(View):
    def get(self, request):

        user = request.user
        cart_name = []
        user_cart = CartItem.objects.filter(user_id=request.user.id, cart_is_del=0).first()
        if not user_cart:
            return redirect(reverse("app_cart:cart_page"))
        user_cart.cart_is_del = 1
        user_cart.save()
        game_kind_num = user_cart.sku_id.all()

        sum_cart_price = 0
        sum_num = 0
        for i in game_kind_num:
            sum_cart_price += i.num * i.sku_id.sku_price
            discout_price = sum_cart_price * i.sku_id.sku_discount
            sum_num += i.num
        sum_cart_price = round(sum_cart_price, 2)
        discout_price = round(discout_price, 2)
        save_price = round(sum_cart_price - discout_price, 2)

        '''
        将信息传到 订单表中
        '''
        information = OrderMessage.objects.create(order_pay_methods="微信支付", user_id=user, order_all_money=sum_cart_price,
                                                  order_all_number=sum_num, order_pay_state=False, order_create_time=datetime.datetime.now())
        for i in game_kind_num:
            commodity = OrderCommodity.objects.create(order_id_id=information.order_id, sku_id_id=i.sku_id.sku_id,
                                                      oc_number=i.num, oc_price=i.sku_id.sku_price*i.num, oc_comment='默认好评')

        return render(request, "orders_page.html", locals())




class OrderShow(View):
    def get(self, request):
        user = request.user

        obj = OrderMessage.objects.filter(user_id=user)
        return render(request, "orders_show.html", locals())


class DelOrder(View):
    def get(self, request, *args):
        user = request.user

        try:
            id = int(args[0])
            obj_del = OrderMessage.objects.filter(user_id=user, order_id=id).first()
            obj_del.order_pay_state = -1
            obj_del.save()
            obj = OrderMessage.objects.filter(user_id=user)
            return redirect(reverse('app_order:order_show'))
        except Exception:
            return redirect(reverse('app_commidity:index'))



class OrderLast(View):
    def get(self, request, *args):
        id = args[0]
        information = OrderMessage.objects.filter(order_id=id, user_id=request.user).first()
        # game_kind_num = information.filter("ordercommodity__sku_id")
        sku_kind_num = information.ordercommodity_set.all()
        print(sku_kind_num)
        return render(request, 'orders_last.html', locals())


