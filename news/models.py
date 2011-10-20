# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymodels

class News(models.Model):
    date = models.DateField(u'Дата')
    title = models.CharField(u'Заголовок',max_length=120)
    
    content = tinymodels.HTMLField(u'Текст новости')
#    content = models.TextField(u'Текст новости')

    show = models.BooleanField(u'Опубликовать',default=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/news/%d/' % self.pk

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ('-date',)