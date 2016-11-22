# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.
class DesignType(models.Model):
    #камни, глина, бисер...
    name = models.CharField('Тип изделия', max_length=50, blank=False, unique=True)
    is_displayed = models.BooleanField('Отображать', default=True)

    class Meta:
        verbose_name_plural = 'Состав'

    def __str__(self):
        return self.name


class Category(models.Model):
    #браслет, серьги...
    name = models.CharField(max_length=30, blank=False, unique=True)
    is_displayed = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    is_displayed = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Good(models.Model):
    category = models.ForeignKey('Category')
    design_types = models.ManyToManyField('DesignType')
    colors = models.ManyToManyField('Color')
    title = models.CharField(max_length=50, blank=False)
    short_description = models.CharField(max_length=100)
    full_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    full_img_uri = models.ImageField(upload_to='goods_img', blank=True)
    preview_img_uri = models.ImageField(upload_to='goods_img', blank=True)
    data_created = models.DateTimeField(default=timezone.now())
    amount = models.IntegerField(default=1)
    is_displayed = models.BooleanField(default=True)


# class Users(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(default='your@email.here')
#     phone_number = models.CharField(max_length=15, default='+7123456789')
#     password = models.CharField(max_length=20)
#     date_register = models.DateTimeField(default=timezone.now())
#
#
# class Cart(models.Model):
#     user_id = models.ForeignKey('Users')
#     good_id = models.ForeignKey('Goods')
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.IntegerField()
#     done = models.BooleanField(default=False)


