# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class NoticePost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

# Create your models here.


