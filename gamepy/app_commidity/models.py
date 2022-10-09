from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models



class CommodityKind(models.Model):
    com_id = models.AutoField(primary_key=True, verbose_name='商品种类id')
    com_name = models.CharField(max_length=20, unique=True, verbose_name='商品种类名称')
    com_logo = models.CharField(max_length=20, unique=True, verbose_name='商品种类logo')
    com_picture = models.ImageField(upload_to='image', verbose_name='商品种类图片')


class CommoditySpu(models.Model):
    spu_id = models.AutoField(primary_key=True, verbose_name='商品spuid')
    spu_name = models.CharField(max_length=20, unique=True, verbose_name='商品spu名称')
    spu_details = models.TextField(verbose_name='详情')

class CommoditySku(models.Model):
    sku_id = models.AutoField(primary_key=True, verbose_name='商品skuid')
    sku_name = models.CharField(max_length=20, unique=True, verbose_name='商品sku名称')
    sku_brief_introduction = models.TextField(verbose_name='商品简介')
    sku_price = models.FloatField(verbose_name='商品价格')
    sku_unit = models.CharField(max_length=10, verbose_name='商品单位')
    sku_stock = models.IntegerField(verbose_name='商品库存')
    sku_slaes = models.IntegerField(verbose_name='商品销量')
    sku_state = models.BooleanField(verbose_name='商品状态')
    com_id = models.ForeignKey(to='CommodityKind', on_delete=models.CASCADE, verbose_name='种类id')
    spu_id = models.ForeignKey(to='CommoditySpu', on_delete=models.CASCADE, verbose_name='spu_id')





class CommdityPicture(models.Model):
    comm_id = models.AutoField(primary_key=True, verbose_name='图片id')
    comm_picture = models.ImageField(upload_to='image', verbose_name='图片')
    comm_video = models.FileField(upload_to='image', verbose_name='视频')
    sku_id = models.ForeignKey(to='CommoditySku', on_delete=models.CASCADE, verbose_name='sku_id')


class HomeCarousel(models.Model):
    home_car_id = models.AutoField(primary_key=True, verbose_name='轮播id')
    home_car_picture = models.ImageField(upload_to='image', verbose_name='轮播图片')
    home_car_index = models.IntegerField(verbose_name='顺序索引')
    sku_id = models.ForeignKey(to='CommoditySku', on_delete=models.CASCADE, verbose_name='sku_id')


class HomePromotion(models.Model):
    home_pro_id = models.AutoField(primary_key=True, verbose_name='首页促销活动id')
    home_pro_picture = models.ImageField(upload_to='image', verbose_name='图片')
    home_pro_index = models.IntegerField(verbose_name='顺序索引')
    sku_id = models.ForeignKey(to='CommoditySku', on_delete=models.CASCADE, verbose_name='sku_id')
    home_pro_url = models.ImageField(upload_to='image', verbose_name='活动url')


class HomeDisplay(models.Model):
    home_dis_id = models.AutoField(primary_key=True, verbose_name='首页分类商品展示id')
    home_dis_identification = models.BooleanField(verbose_name='展示标识')
    home_dis_index = models.IntegerField(verbose_name='索引')
    sku_id = models.ForeignKey(to='CommoditySku', on_delete=models.CASCADE, verbose_name='sku_id')
    com_id = models.ForeignKey(to='CommodityKind', on_delete=models.CASCADE, verbose_name='商品种类id')
