from django.shortcuts import render, redirect
from .models import UserInfo
from hashlib import sha1
# Create your views here.
def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    # 接受用户输入
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('pwd')
    upwd2=post.get('cpwd')
    uemail=post.get('email')
    # 判断密码是否一致
    if upwd!=upwd2:
        return redirect('/user/register/')
    # 加密
    s1=sha1()
    s1.update(upwd.encode("utf8"))
    upwd3=s1.hexdigest()
    #创建对象
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    uemail=uemail
    try:
        user.save()
    except Exception as e:
        raise

    # 转到登录页面
    return redirect('/user/login')

def login(request):
    return render(request, 'df_user/login.html')