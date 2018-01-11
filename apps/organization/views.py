# encoding: utf-8
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
# 处理课程机构列表的view
from .models import CourseOrg, CityDict


class OrgView(View):
    def get(self,request):
        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()
        # 总共有多少家机构使用count进行统计
        org_nums = all_orgs.count()
        # 取出所有的城市
        all_city = CityDict.objects.all()

        return render(request, "org-list.html", {
            "all_orgs":all_orgs,
            "all_city": all_city,
            "org_nums": org_nums,
        })