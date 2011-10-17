# -*- coding: utf-8 -*-
from django.db import models
import datetime
from tinymce import models as tm
from settings import STATICFILES_DIRS

class Color(models.Model):
    name = models.TextField(u'Цвет кирпича')
    def __unicode__(self):
        return self.name

view_c = ((u'Лицевой',u'Лицевой'),(u'Рядовой',u'Рядовой'))

class Brick(models.Model):
    name = models.TextField(u'Имя')
    view = models.TextField(u'Вид',choices=view_c)
    width = models.TextField(u'Толшина')

    def __unicode__(self):
        return self.name

class Price(models.Model):
    order = models.PositiveSmallIntegerField(u'Порядок')
    brick = models.ForeignKey(Brick,verbose_name=u'Кирпич')
    mark = models.SmallIntegerField(u'Марка')
    color = models.ForeignKey(Color,verbose_name=u'Цвет кирпича')
    price = models.FloatField(u'Цена')

    def __unicode__(self):
        return u'Позиция № %d, %s %s %d' % (self.order,self.brick,self.color,self.mark)

class PriceList(models.Model):
    date = models.DateField(u'Дата прайса',default=datetime.date.today())
    file = models.FileField(u'Файл с прайсом',upload_to=STATICFILES_DIRS[0])
    price = models.ManyToManyField(Price,verbose_name=u'Позиция')
        
    def __unicode__(self):
        return u'Прайс лист от %s' % self.date.isoformat()
