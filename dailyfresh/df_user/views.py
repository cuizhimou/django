#coding=utf-8
from django.shortcuts import render,redirect
from models import  *
from hashlib import sha1

def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    #接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    #判断两次密码的输入
    if upwd != upwd2:
        return redirect('/user/register/')
    #密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd3=s1.hexdigest()
    #创建模型类对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    #转到登录页面
    return redirect('/user/login.html')