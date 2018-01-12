# encoding: utf-8
from courses.views import CourseListView, CourseDetailView

__author__ = 'mtianyan'
__date__ = '2018/1/13 0013 00:39'

from django.conf.urls import url

urlpatterns = [
    # 课程列表url
    url(r'^list/$', CourseListView.as_view(), name="list"),
    # 课程详情页
    url(r'^course/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

]

