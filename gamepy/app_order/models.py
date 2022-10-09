from django.db import models
# Create your models here.


class OrderMessage(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='订单id')
    order_pay_methods = models.CharField(max_length=20, unique=True, verbose_name='支付方式')
    add_id = models.ForeignKey(to='app_user.Address', on_delete=models.CASCADE, verbose_name='地址id')
    user_id = models.ForeignKey(to='app_user.User', on_delete=models.CASCADE, verbose_name='用户id')
    order_all_money = models.FloatField(verbose_name='总金额')
    order_all_number = models.IntegerField(verbose_name='总数量')
    # order_freight
    order_pay_state = models.BooleanField(verbose_name='支付状态')
    order_create_time = models.DateTimeField(verbose_name='订单创建时间')


class OrderCommodity(models.Model):
    oc_id = models.AutoField(primary_key=True, verbose_name='订单商品id')
    order_id = models.ForeignKey(to='OrderMessage', on_delete=models.CASCADE, verbose_name='订单id')
    add_id = models.ForeignKey(to='app_user.Address', on_delete=models.CASCADE, verbose_name='地址id')
    sku_id = models.ForeignKey(to='app_commidity.CommoditySku', on_delete=models.CASCADE, verbose_name='sku_id')
    oc_number = models.IntegerField(verbose_name='商品数量')
    oc_price = models.FloatField(verbose_name='商品价格')
    oc_comment = models.TextField(verbose_name='评论')