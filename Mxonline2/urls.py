# encoding: utf-8
"""Mxonline2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# 导入x admin，替换admin
import xadmin
from django.views.generic import TemplateView
# from users.views import user_login
# 换用类实现
from users.views import LoginView, RegisterView, ActiveUserView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),

    # 登录页面跳转url login不要直接调用。而只是指向这个函数对象。
    # url('^login/$',user_login, name="login")

    # 基于类方法实现登录,这里是调用它的方法
    url('^login/$', LoginView.as_view(), name="login"),

    # 验证码 url配置
    url(r'^captcha/', include('captcha.urls')),
    # 注册url
    url("^register/", RegisterView.as_view(), name="register"),
    # 激活用户url
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(), name= "user_active")
]
