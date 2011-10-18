# -*- coding: utf-8 -*-
from django.db import models
import datetime
from tinymce import models as tm
from settings import STATICFILES_DIRS

chars = u"""Морозостойкость - до F 50
Водопоглощение - 8-12%
Вес - %s кг.
Пустотность - 30%
Удельная эффективная ественная активность радионуклидов - 127,9 Бк/кг
Теплопроводность - 0,34 Вт/м,с"""

GOST = u'ГОСТ 530-2007'

class Color(models.Model):
    name = models.CharField(u'Цвет кирпича',max_length=50)
    cold = models.IntegerField(u'Морозостойкость',default=50)
    water = models.CharField(u'Водопоглощение',default=u'8-12',max_length=50)
    void = models.IntegerField(u'Пустотность',default=u'30')
    radia = models.CharField(u'Удельная эффективная естетвенная активность радионуклидов',default=u'127,9',max_length=50)
    heat = models.CharField(u'Теплопроводность',default=u'0,34',max_length=50)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Цвет кирпича'
        verbose_name_plural = u'Цвет кирпичей'

view_c = ((u'Лицевой',u'Лицевой'),(u'Рядовой',u'Рядовой')) #Строительный (Рядовой)

class Width(models.Model):
    name = models.CharField(u'Название',max_length=60)
    size = models.CharField(u'Размеры',max_length=60)
    weight = models.CharField(u'Вес',max_length=60)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Ширина кирпича'
        verbose_name_plural = u'Ширина кирпичей'

class MarkPrice(models.Model):
    mark = models.CharField(u'Марка',max_length=60)
    price = models.FloatField(u'Цена')

    def __unicode__(self):
        return u'%s - %.2f' % (self.mark,self.price)


class PriceList(models.Model):
    date = models.DateField(u'Дата прайса',default=datetime.date.today())
    file = models.FileField(u'Файл с прайсом',upload_to=STATICFILES_DIRS[0],blank=True)

    class Meta:
        verbose_name = u'Прайс-лист'
        verbose_name_plural = u'Прайс-листы'

    def __unicode__(self):
        return u'Прайс лист от %s' % self.date.isoformat()


class Brick(models.Model):
    order = models.PositiveSmallIntegerField(u'Порядок')
    view = models.CharField(u'Вид',choices=view_c,max_length=60)
    width = models.ForeignKey(Width,verbose_name=u'Толшина')
    color = models.ForeignKey(Color,verbose_name=u'Цвет кирпича')
    tara = models.IntegerField(u'Кол-во кирпича на 1 поддоне')
    mark_price = models.ManyToManyField(MarkPrice,verbose_name=u'Марка и цена',blank=True)
    price = models.ForeignKey(PriceList,verbose_name=u'Прайс',default=PriceList.objects.latest('date'))

    class Meta:
        verbose_name = u'Кирпич из прайса'
        verbose_name_plural = u'Кирпичи в прайсах'

    def name(self):
        return u'Кирпич керамический %s пустотелый %s' % (self.view.lower(),self.width.name.lower())

    def __unicode__(self):
        return u'Позиция № %d, %s' % (self.order,self.name())
