# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class listt(models.Model):
    class Meta:
        verbose_name = u'模块管理'
        verbose_name_plural = u'模块管理'

    name = models.CharField(u'类别', max_length=20)
    sortId = models.IntegerField(u'序列ID', default=0)

    def __str__(self):
        return self.name	

class yunwei(models.Model):
    class Meta:
        verbose_name = u'项目管理'
        verbose_name_plural = u'项目管理'
    name = models.CharField(u'标题', max_length=30)
    link = models.CharField(u'链接', max_length=40)
    title = models.ForeignKey(listt, on_delete = models.CASCADE)
	
    def __str__(self):
        return self.name

class yunwei_user(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(u'姓名', max_length=50)

    def __str__(self):
        return self.username

