# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.
class DesignType(models.Model):
    #камни, глина, бисер...
    name = models.CharField(max_length=50)
    is_displayed = models.BooleanField(default=True)

    def __str__(self):
        return ('Design: {}'.format(self.name))


class Category(models.Model):
    #браслет, серьги...
    name = models.CharField(max_length=30)
    is_displayed = models.BooleanField(default=True)

    def __str__(self):
        return ('Category: {}'.format(self.name))


class Color(models.Model):
    name = models.CharField(max_length=20)
    is_displayed = models.BooleanField(default=True)

    def __str__(self):
        return ('Color: {}'.format(self.name))


class GoodDescription(models.Model):
    short_description = models.CharField(max_length=100)
    full_description =models.TextField()


class Goods(models.Model):
    category_id = models.ForeignKey('Category')
    design_type_id = models.ManyToManyField('DesignType')
    color_id = models.ManyToManyField('Color')
    title = models.CharField(max_length=30)
    good_description = models.ForeignKey('GoodDescription')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    full_img_uri = models.URLField()
    preview_img_uri = models.URLField()
    data_created = models.DateTimeField(default=timezone.now())
    amount = models.IntegerField()
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


