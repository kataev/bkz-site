# -*- coding: utf-8 -*-
from django.db import models
from bkz.priceList.models import *

class Product(models.Model):
    brick = models.ForeignKey(Brick)
    color = models.ManyToManyField(Color)
    about = models.TextField()
#    image = models.ImageField()
    def __unicode__(self):
        return unicode(self.brick)
