# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
import sys
from .models import yunwei, listt, yunwei_user
from .forms import LoginForm

# Create your views here.
# login
def login(request):
	if request.method == 'POST':
		loginform = LoginForm(request.POST)
		if loginform.is_valid():
			username = loginform.cleaned_data['username']
			password = loginform.cleaned_data['password']
			user = yunwei_user.objects.filter(username__exact = username,password__exact = password)
			if user:
				response = HttpResponseRedirect('/web/index/')
				#将username写入浏览器cookie,失效时间为3600
				response.set_cookie('username', uaername, 3600)
				return response
			else:
				return HttpResponseRedirect('/web/login/')
	else:
		loginform = LoginForm()
		print(loginform)
	return render_to_response('login.html',{'loginform': loginform})


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

