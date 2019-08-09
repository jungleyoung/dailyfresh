from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import UserInfo
from hashlib import sha1
# Create your views here.

def index(request):
    return render(request,'df_user/index.html')

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
    user.uemail=uemail
    try:
        user.save()
    except Exception as e:
        raise

    # 转到登录页面
    return redirect('/user/login')

def register_exist(request):
    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})
def login_handle(request):
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    jizhu=post.get('jizhu',0)
    users=UserInfo.objects.filter(uname=uname)
    # print(uname)
    if len(users)==1:
        s1=sha1()
        s1.update(upwd.encode("utf8"))
        if s1.hexdigest()==users[0].upwd:
            red=HttpResponseRedirect('/user/info/')
            #记住用户名
            if jizhu!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)

            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context = {'title': '用户登录',
                       'error_name': 0 ,
                       'error_pwd': 1,
                       'uname': uname,
                       'upwd': upwd, }
            return render(request,'df_user/login.html', context)
    else:
        # print(users[1].uname)
        # print(users)
        # print(len(users))
        context={'title':'用户登录',
                 'error_name':1,
                 'error_pwd':0,
                 'uname':uname,
                 'upwd':upwd,}
        return render(request,'df_user/login.html',context)

def info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).uemail
    context={
        'titile':'用户中心',
        'user_email':user_email,
        'user_name':request.session['user_name']
    }
    print(user_email)
    return render(request, 'df_user/user_center_info.html',context)

def cart(request):
    return  render(request,'df_user/cart.html')

def order(request):
    return render(request,'df_user/user_center_order.html')

def login(request):
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登录',
             'error_name':0,
             'error_pwd':0,
             'uname':uname}
    return render(request, 'df_user/login.html',context)

def site(request):
    user=UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        post=request.POST
        user.urer=post.get('urer')
        user.uaddr=post.get('uaddress')
        user.upocode=post.get('upocode')
        user.uphone=post.get('uphone')
        user.save()

    context={'title':'用户中心','user':user}
    return render(request,'df_user/user_center_site.html',context)