from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    用户信息表
    """
    # id = models.AutoField(primary_key=True, verbose_name='用户id')
    # userId = models.CharField(max_length=20, unique=True)
    # userPwd = models.CharField(max_length=20)
    # userEmail = models.CharField(max_length=32, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    # userAcitvate = models.BooleanField()
    # userPermission = models.BooleanField()

    # def __str__(self):
    #     return self.username


class Address(models.Model):
    add_id = models.AutoField(primary_key=True, verbose_name='地址id')
    add_addressee = models.CharField(max_length=20, unique=True, verbose_name='收件人')
    add_receive = models.CharField(max_length=32, verbose_name='收件地址')
    # addPost = models.CharField(max_length=32)
    add_iphone = models.CharField(max_length=32, verbose_name='联系方式')
    add_default = models.BooleanField(verbose_name='地址是否默认')
    user_id = models.ForeignKey(to='User', on_delete=models.CASCADE, verbose_name='用户id')