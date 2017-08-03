# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import sys
from .models import yunwei, listt

# Create your views here.
def index(request):
	List = []
	data = {}
	data_name = yunwei.objects.all()
	for name in data_name:
		link = yunwei.objects.values_list('link').filter(name__contains = name)
		title_id = yunwei.objects.values_list('title_id').filter(name__contains = name)
		title_list = listt.objects.values_list('name').filter(id__contains = title_id[0][0])
		title = title_list[0][0]
		if title in data.keys():
			data[title].append({name:link[0][0]})
		else:
			data[title] = [{name:link[0][0]}]
	return render(request, 'index.html', {'data': data})

