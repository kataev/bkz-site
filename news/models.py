# -*- coding: utf-8 -*-
from django.db import models
import datetime
import pytils
from tinymce import models as tm

class News(models.Model):
    date = models.DateField(u'Дата')
    title = models.CharField(u'Заголовок',max_length=120)
    content = models.TextField(u'Текст новости')

    show = models.BooleanField(u'Опубликовать?',default=False)

    def get_absolute_url(self):
        return '/news/%d/' % self.pk

    def d(self):
        return pytils.dt.ru_strftime(u'%d %B %Y',inflected=True,date=self.date)

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ('-date',)