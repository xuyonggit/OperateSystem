# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from .models import yunwei, listt, yunwei_user
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
import sys
# Create your views here.


# login
@csrf_exempt
def login(request):
    if request.method == 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
            user = yunwei_user.objects.filter(username__exact=username, password__exact=password)
            if user:
                response = HttpResponseRedirect('/web/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/web/login/')
    else:
        lf = LoginForm()
    return render_to_response('login.html', {'lf': lf})

@csrf_exempt
def index(request):
    List = []
    data = {}
    data_name = yunwei.objects.all()
    for name in data_name:
        link = yunwei.objects.values_list('link').filter(name__contains=name)
        title_id = yunwei.objects.values_list('title_id').filter(name__contains=name)
        title_list = listt.objects.values_list('name').filter(id__contains=title_id[0][0])
        title = title_list[0][0]
        if title in data.keys():
            data[title].append({name: link[0][0]})
        else:
            data[title] = [{name: link[0][0]}]
    if request.COOKIES:
        cook = request.COOKIES['username']
        return render(request, 'index.html', {'data': data, 'user': cook})
    else:
        return HttpResponseRedirect('/web/login/')
