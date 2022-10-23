from django.contrib import admin

# Register your models here.


from django.contrib import admin
from app_cart.models import *  # models模块中定义的图书表的信息


# admin.site.register(User)
# admin.site.register(Address)

class SkuNumAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('sku_id', 'num')}),
    )




class CartItemAdmin(admin.ModelAdmin):
    # 必须写成list_display  列表中的内容要与数据库字段名一致
    # list_display = ['cart_is_del']
    fieldsets = (
        (None, {'fields': ('cart_is_del',  'user_id', 'cart_count', 'sku_id')}),
    )
    filter_horizontal = ('sku_id',)


admin.site.register(CartItem, CartItemAdmin)
admin.site.register(SkuNum, SkuNumAdmin)


