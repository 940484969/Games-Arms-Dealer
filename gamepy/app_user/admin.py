

# Register your models here.

from django.contrib import admin
from app_user.models import Address, User  # models模块中定义的图书表的信息


# admin.site.register(User)
# admin.site.register(Address)


class AddressAdmin(admin.ModelAdmin):
    # 必须写成list_display  列表中的内容要与数据库字段名一致
    list_display = ['add_id', 'add_addressee', 'add_receive', 'add_iphone', 'add_default', 'user_id']


class UserAdmin(admin.ModelAdmin):
    list_display = ['password', 'last_login', 'is_superuser', 'username', 'email', 'is_staff', 'is_active',
                    'date_joined', 'id']


# 修改模型类BookInfo的注册代码
admin.site.register(Address, AddressAdmin)
admin.site.register(User, UserAdmin)
