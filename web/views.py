# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import yunwei, listt, yunwei_user
from .forms import LoginForm, resetpasswd
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import sys
# Create your views here.
from .conn_mongo import mongo_query
import json


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
                return HttpResponse('密码错误，请重新输入')
    else:
        lf = LoginForm()
    return render_to_response('login.html', {'lf': lf})


# 主页
@csrf_exempt
def index(request):
    List = []
    data = {}
    templates = []
    title_list = listt.objects.order_by('sortId')
    for title in title_list:
        templates.append(title)
        title_id = listt.objects.values('id').filter(name=title)
        res = yunwei.objects.values('name', 'link').filter(title_id=title_id)
        data[title] = res
    if 'username' in request.COOKIES:
        cook = request.COOKIES['username']
        user_name = yunwei_user.objects.values_list('name').filter(username__contains=cook)[0][0]
        return render(request, 'index.html', {'templates': templates, 'data': data, 'user': user_name})
    else:
        return HttpResponseRedirect('/web/login/')


# 版本查询
@csrf_exempt
def version(request):
    if request.method == 'POST':
        if request.GET['action'] == "get_vm":
            if request.POST['i_version'] == "":
                i_version = 328
            else:
                i_version = request.POST['i_version']
            if request.POST['i_type'] == "":
                i_type = ""
            else:
                i_type = request.POST['i_type']
        dic1 = {'i_version': i_version, 'i_type': i_type}
        query_data = mongo_query(List=dic1)
        del query_data["_id"]
        return HttpResponse(json.dumps(query_data))
    else:
        return render(request, 'version.html')


# 密码重置
@csrf_exempt
def lostpasswd(request):
    if request.method == 'GET':
        lf = resetpasswd()
        return render(request, 'resetpasswd.html', {'lf': lf})