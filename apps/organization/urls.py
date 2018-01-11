# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/1/12 0012 06:20'

# encoding: utf-8
from organization.views import OrgView, AddUserAskView
from django.conf.urls import url

urlpatterns = [
    # 课程机构列表url
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    # 添加我要学习
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask")
]