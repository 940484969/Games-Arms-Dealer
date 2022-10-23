from django.db import models

# Create your models here.

class SkuNum(models.Model):
    num_id = models.AutoField(primary_key=True, verbose_name='购物车id')
    sku_id = models.ForeignKey(to='app_commidity.CommoditySku', on_delete=models.CASCADE, verbose_name='sku')
    num = models.IntegerField(default=1)



class CartItem(models.Model):
    cart_id = models.AutoField(primary_key=True, verbose_name='购物车id')
    cart_is_del = models.SmallIntegerField(verbose_name='isdelete 标志位？')
    user_id = models.ForeignKey(to='app_user.User', on_delete=models.CASCADE, verbose_name='user')
    cart_count = models.IntegerField(verbose_name='全部数量')
    sku_id = models.ManyToManyField(to='app_cart.SkuNum', verbose_name='种类数量')




