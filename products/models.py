from django.db import models

# Create your models here.

# 根据一下建立项目
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    # 链接
    image_url = models.CharField(max_length=2083)

# 数据库添加offer
class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()