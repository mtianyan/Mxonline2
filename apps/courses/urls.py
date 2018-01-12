# encoding: utf-8
from courses.views import CourseListView

__author__ = 'mtianyan'
__date__ = '2018/1/13 0013 00:39'

from django.conf.urls import url

urlpatterns = [
    # 课程列表url
    url(r'^list/$', CourseListView.as_view(), name="list"),

]

