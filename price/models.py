# -*- coding: utf-8 -*-
from django.db import models
import datetime
from tinymce import models as tm

class Price(models.Model):
    date=models.DateField(u'Дата прайса',default=datetime.date.today())
#    file = models.FileField(u'Файл с прайсом')
    price = tm.HTMLField()

class People(models.Model):
    name = models.TextField(u'Имя')
    place = models.TextField()