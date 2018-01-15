# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/1/9 0009 20:28'

from .models import Course, Lesson, Video, CourseResource, BannerCourse
import xadmin



# 课程直接添加章节
class LessonInline(object):
    model = Lesson
    extra = 0
class CourseResourceInline(object):
    model = CourseResource
    extra = 0

# Course的admin管理器
class CourseAdmin(object):
    list_display = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']
    ordering = ['-click_nums']
    readonly_fields =['click_nums']
    exclude = ['fav_nums']
    # 课程直接添加章节
    inlines = [LessonInline,CourseResourceInline]
    list_editable = [ 'degree','desc',]
    refresh_times = [3,5]
    # 富文本
    style_fields = {"detail":"ueditor"}
    import_excel = True

    # 过滤列表中的数据
    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs
    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        # 字段联动
        obj = self.new_obj
        # 新增课程还没有保存，统计的课程数少一个
        obj.save()
        # 必须确定存在。
        if obj.course_org is not None:
            # obj实际是一个course对象
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org = course_org).count()
            course_org.save()

    def post(self, request, *args , **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)


# Course的admin管理器
class BannerCourseAdmin(object):
    list_display = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students',
    'get_zj_nums',
        'go_to',
    ]
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_times',
        'students']
    ordering = ['-click_nums']
    readonly_fields =['click_nums']
    exclude = ['fav_nums']
    # 课程直接添加章节
    inlines = [LessonInline,CourseResourceInline]
    # 富文本
    style_fields = {"detail": "ueditor"}

    # 过滤列表中的数据
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'download', 'add_time']


# 将管理器与model进行注册关联
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)