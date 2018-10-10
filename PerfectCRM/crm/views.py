from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from crm import models

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def dashboard(request):
    customer = models.CustomerInfo.objects.all()
    return render(request, 'index.html', locals())


def acc_login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        #user是一个对象
        #验证
        user = authenticate(username=username,password=password)
        if user:
            #登录（已生成session）
            login(request, user)
            #如果有next值就获取next值，没有就跳转到首页
            return redirect(request.GET.get('next','/crm/'))
        else:
            error_msg = '用户名或密码错误！'

    return render(request,'login.html',{'error_msg':error_msg})

def acc_logout(request):
    logout(request)
    return redirect("/crm/login/")



def response(request):
    customer = models.CustomerInfo.objects.all()
    return render(request, 'response.html', locals())

def info(request):
    customer = models.CustomerInfo.objects.all()
    return render(request, 'info.html', locals())

def test1(request):
    customer = models.CustomerInfo.objects.all()
    return render(request, 'test1.html', locals())


@login_required
def table_obj_list(request,app_name, model_name):
    querysets = models.CustomerInfo.objects.all()
    paginator = Paginator(querysets, 2)
    page = request.GET.get('page')
    try:
        querysets = paginator.page(page)
    except PageNotAnInteger:
        querysets = paginator.page(1)
    except EmptyPage:
        querysets = paginator.page(paginator.num_pages)

    return render(request, 'table_obj_list.html', locals())



