# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import listt, yunwei
# class your models here.


class yunweiAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name',)


class listtAdmin(admin.ModelAdmin):
    list_display = ('name', 'sortId')







# Register your models here.

admin.site.register(yunwei, yunweiAdmin)
admin.site.register(listt, listtAdmin)
