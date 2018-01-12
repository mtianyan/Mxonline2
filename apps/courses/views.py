# encoding: utf-8
from django.shortcuts import render
from django.views.generic.base import View

from operation.models import UserFavorite
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


 # 课程详情处理view

class CourseDetailView(View):
    def get(self, request, course_id):
        # 此处的id为表默认为我们添加的值。
        course = Course.objects.get(id=int(course_id))
        # 是否收藏课程
        has_fav_course = False
        has_fav_org = False

        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True
        # 增加课程点击数
        course.click_nums += 1
        course.save()
        tag = course.tag
        if tag:
            # 需要从1开始不然会推荐自己
            relate_courses = Course.objects.filter(tag=tag)[1:2]
        else:
            relate_courses = []


        return render(request, "course-detail.html", {
            "course": course,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,
        })