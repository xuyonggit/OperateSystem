from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import yunwei_user
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt



# login
@csrf_exempt
def login(request):
    if request.method == 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            all_data = lf.clean()  # 获取post数据，例如 {'username': u'yang1', 'password': 111}
            user = yunwei_user.objects.filter(username=all_data['username'], password=all_data['password']).first()
            if user:
                # 写入session
                request.session['IS_LOGIN'] = True
                request.session['uid'] = user.id
                return HttpResponseRedirect("/web/index/")
            else:
                return HttpResponse('密码错误，请重新输入')
    else:
        lf = LoginForm()
    return render_to_response('login.html', {'lf': lf})


# 检查登录状态
def Check_Login(func):
    """
    查看session值用来判断用户是否已经登录
    :param request:
    :return:
    """
    def warpper(request, *args, **kwargs):
        is_login = request.session.get("IS_LOGIN", False)
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/web/login/")
    return warpper


def logout(request):
    request.session.pop('IS_LOGIN', None)
    request.session.pop('uid', None)
    return HttpResponseRedirect("/web/login/")
