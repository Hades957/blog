from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # 定义手机号
    mobile = models.CharField(max_length=11, unique=True, blank=False)
    # 头像信息
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    # 简介信息
    user_desc = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = 'tb_users'  # 表名
        # admin后台显示
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    # 方便展示
    def __str__(self):
        return self.mobile
