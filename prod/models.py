# -*- coding: utf-8 -*-
from django.db import models
from bkz.priceList.models import *
from tinymce import models as tinymodels

class Product(models.Model):
    brick = models.ForeignKey(Brick,verbose_name=u'Кирпич')
    color = models.ManyToManyField(Color,verbose_name=u'Какие цвета в продаже')
    about = tinymodels.HTMLField(u'Текст новости')
#    image = models.ImageField(u'Изображение')
    def __unicode__(self):
        return unicode(self.brick)

    def get_absolute_url(self):
        return '/products/#%d' % self.pk

    class Meta:
        verbose_name = u'Описание продукции'
        verbose_name_plural = u'Описание продукции'
