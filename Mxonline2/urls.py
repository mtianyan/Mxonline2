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
from django.views.static import serve

import xadmin
from django.views.generic import TemplateView
# from users.views import user_login
# 换用类实现
from Mxonline2.settings import MEDIA_ROOT
from organization.views import OrgView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView, \
    IndexView
# from users.views import LoginUnsafeView
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name="index"),

    # 登录页面跳转url login不要直接调用。而只是指向这个函数对象。
    # url('^login/$',user_login, name="login")

    # 基于类方法实现登录,这里是调用它的方法
    url('^login/$', LoginView.as_view(), name="login"),

    # 不安全的sql注入
    # url('^login/', LoginUnsafeView.as_view(), name='login'),

    # 验证码 url配置
    url(r'^captcha/', include('captcha.urls')),
    # 注册url
    url("^register/", RegisterView.as_view(), name="register"),
    # 激活用户url
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(), name= "user_active"),

    # 忘记密码
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # 重置密码urlc ：用来接收来自邮箱的重置链接
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    # 修改密码url; 用于passwordreset页面提交表单
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # 课程机构app的url配置
    url(r"^org/", include('organization.urls',namespace="org")),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT }),
# 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
#     url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT }),
    # 课程app的url配置
    url(r"^course/", include('courses.urls', namespace="course")),

    # user app的url配置
    url(r"^users/", include('users.urls', namespace="users")),

    # 退出功能url
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    # 富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

    url(r'^favicon\.ico$', favicon_view),
]

# 全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'