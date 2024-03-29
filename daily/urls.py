"""daily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dailyfresh.views import *
from df_goods.views import index as index1
# from dailyfresh.views import order,register,register_handle,login,info,login_handle
from django.urls import path,include
# from . import dailyfresh

urlpatterns = [
    path('index/',index1),
    path('',index),
    path('user/index/',index),
    path('admin/', admin.site.urls),
    path('user/register/',register),
    path('user/register_handle',register_handle),
    path('user/login/',login),
    path('user/login_handle',login_handle),
    path('user/info/',info),
    path('user/order/',order),  
    path('user/cart/',cart),
    path('user/site/',site),
    path('user/list/',list),
    path('user/place_order/',place_order),
    path('tinymce/',include('tinymce.urls')),
    # path('user/',include('dailyfresh.urls'))
]
