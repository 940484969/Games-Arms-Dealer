from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app_commidity.models import *  # models模块中定义的图书表的信息


# admin.site.register(User)
# admin.site.register(Address)


class CommodityKindAdmin(admin.ModelAdmin):
    # 必须写成list_display  列表中的内容要与数据库字段名一致
    list_display = ['com_id', 'com_name', 'com_logo', 'com_picture']


class CommoditySpuAdmin(admin.ModelAdmin):
    list_display = ['spu_id', 'spu_name', 'spu_details']


class CommoditySkuAdmin(admin.ModelAdmin):
    list_display = ['sku_id', 'sku_name', 'sku_brief_introduction', 'sku_price', 'sku_unit', 'sku_stock', 'sku_slaes',
                    'sku_state', 'com_id_id', 'spu_id_id']


class CommdityPictureAdmin(admin.ModelAdmin):
    list_display = ['comm_id', 'comm_picture', 'comm_video', 'sku_id_id']


class HomeCarouselAdmin(admin.ModelAdmin):
    list_display = ['home_car_id', 'home_car_picture', 'home_car_index', 'sku_id_id']


class HomePromotionAdmin(admin.ModelAdmin):
    list_display = ['home_pro_id', 'home_pro_picture', 'home_pro_index', 'sku_id_id', 'home_pro_url']



class HomeDisplayAdmin(admin.ModelAdmin):
    list_display = ['home_dis_id', 'home_dis_identification', 'home_dis_index', 'sku_id_id', 'com_id_id']



# 修改模型类BookInfo的注册代码
admin.site.register(CommodityKind, CommodityKindAdmin)
admin.site.register(CommoditySpu, CommoditySpuAdmin)
admin.site.register(CommoditySku, CommoditySkuAdmin)
admin.site.register(CommdityPicture, CommdityPictureAdmin)
admin.site.register(HomeCarousel, HomeCarouselAdmin)
admin.site.register(HomePromotion, HomePromotionAdmin)
admin.site.register(HomeDisplay, HomeDisplayAdmin)
