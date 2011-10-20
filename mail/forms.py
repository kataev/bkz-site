# -*- coding: utf-8 -*-
__author__ = 'bteam'
from dojango import forms
from models import *

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
