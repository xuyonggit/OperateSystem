# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . import models
# class your models here.

class yunweiAdmin(admin.ModelAdmin):
	list_display = ('name', 'link')		# list
	search_fields = ('name',)















# Register your models here.

admin.site.register(models.yunwei, yunweiAdmin)
admin.site.register(models.listt)
