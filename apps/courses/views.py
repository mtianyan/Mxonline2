# encoding: utf-8
from django.shortcuts import render
from django.views.generic.base import View
from .models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class CourseListView(View):
    def get(self, request):
        # 以时间排倒序实现最新。-号代表降序排列
        all_course = Course.objects.all().order_by("-add_time")

        # 热门课程推荐
        hot_courses = Course.objects.all().order_by("-students")[:3]

        # 课程进行排序：学习人数，点击数
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_course = all_course.order_by("-students")
            elif sort == "hot":
                all_course = all_course.order_by("-click_nums")

        # 对课程进行分页
        # 尝试获取前台get请求传递过来的page参数
        # 如果是不合法的配置参数默认返回第一页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # 这里指从allorg中取五个出来，每页显示5个
        p = Paginator(all_course,6 , request=request)
        courses = p.page(page)
        return render(request, "course-list.html", {
            "all_course":courses,
            "sort":sort,
            "hot_courses":hot_courses
        })