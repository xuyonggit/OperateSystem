# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .main import Main
# Create your views here.


# 主页
@csrf_exempt
def index(requests):
    l = [69]
    data = Main().get_list(l)
    return render(requests, 'gintong.html', {'data': data})