# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .basees.user import getUserInfoWithId
from .basees.dates import getAllDataBy_sortId
from .Login import Check_Login
# Create your views here.


# 主页
@Check_Login
def index(request):
    # 获取所有数据
    templates, data = getAllDataBy_sortId()
    # 获取登录用户名
    uname = getUserInfoWithId(request.session.get('uid', False))['name']
    return render(request, 'index.html', {'templates': templates, 'data': data, 'user': uname})


# 密码重置
