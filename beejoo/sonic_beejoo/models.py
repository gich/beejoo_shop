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

    class Meta:
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    is_displayed = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Цвет'

    def __str__(self):
        return self.name


class Good(models.Model):
    category = models.ForeignKey('Category')
    design_types = models.ManyToManyField('DesignType')
    colors = models.ManyToManyField('Color',related_name='all_colors')
    title = models.CharField(max_length=50, blank=False)
    short_description = models.CharField(max_length=100)
    full_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    img_uri = models.ImageField(upload_to='goods_img', blank=True)
    img_second_uri = models.ImageField(upload_to='goods_img', blank=True)
    data_created = models.DateTimeField(default=timezone.now())
    amount = models.IntegerField(default=1)
    slug = models.SlugField(max_length=50, blank=False, unique=True)
    is_displayed = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Товар'


class Order(models.Model):
    good_id = models.ForeignKey('Good')
    quantity = models.IntegerField()
    total_sum = models.IntegerField()
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Заказ'


