from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app_order.models import OrderMessage, OrderCommodity  # models模块中定义的图书表的信息


# admin.site.register(User)
# admin.site.register(Address)


class OrderMessageAdmin(admin.ModelAdmin):
    # 必须写成list_display  列表中的内容要与数据库字段名一致
    list_display = ['order_id', 'order_pay_methods', 'add_id_id', 'user_id_id', 'order_all_money', 'order_all_number', 'order_pay_state', 'order_create_time']


class OrderCommodityAdmin(admin.ModelAdmin):
    list_display = ['oc_id', 'order_id_id', 'add_id_id', 'sku_id_id', 'oc_number', 'oc_price', 'oc_comment']


# 修改模型类BookInfo的注册代码
admin.site.register(OrderMessage, OrderMessageAdmin)
admin.site.register(OrderCommodity, OrderCommodityAdmin)
