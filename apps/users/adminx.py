# encoding: utf-8
from crispy_forms.layout import Fieldset
from django.contrib.auth.models import Group, Permission

from operation.models import CourseComments, UserFavorite, UserMessage, UserCourse, UserAsk
from organization.models import CityDict, Teacher, CourseOrg
from xadmin.layout import Main, Row, Side
from xadmin.models import Log
from xadmin.plugins.auth import UserAdmin
from django.utils.translation import ugettext as _
__author__ = 'mtianyan'
__date__ = '2018/1/9 0009 17:31'

import xadmin
from xadmin import views
from courses.models import Course, Lesson, Video, CourseResource
from .models import EmailVerifyRecord, Banner, UserProfile


# 创建X admin的全局管理器并与view绑定。
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# x admin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "天涯明月笙: 慕课后台管理站"
    site_footer = "mtianyan's mooc"
    # 收起菜单
    # menu_style = "accordion"

    # def get_site_menu(self):
    #     return (
    #         {'title': '机构管理', 'menus': (
    #             {'title': '所在城市', 'url': self.get_model_url(CityDict, 'changelist')},
    #             {'title': '机构信息', 'url': self.get_model_url(CourseOrg, 'changelist')},
    #             {'title': '机构讲师', 'url': self.get_model_url(Teacher, 'changelist')},
    #         )},
    #         {'title': '课程管理', 'menus': (
    #             {'title': '课程信息', 'url': self.get_model_url(Course, 'changelist')},
    #             {'title': '章节信息', 'url': self.get_model_url(Lesson, 'changelist')},
    #             {'title': '视频信息', 'url': self.get_model_url(Video, 'changelist')},
    #             {'title': '课程资源', 'url': self.get_model_url(CourseResource, 'changelist')},
    #             {'title': '课程评论', 'url': self.get_model_url(CourseComments, 'changelist')},
    #         )},
    #
    #         {'title': '用户管理', 'menus': (
    #             {'title': '用户信息', 'url': self.get_model_url(UserProfile, 'changelist')},
    #             {'title': '用户验证', 'url': self.get_model_url(EmailVerifyRecord, 'changelist')},
    #             {'title': '用户课程', 'url': self.get_model_url(UserCourse, 'changelist')},
    #             {'title': '用户收藏', 'url': self.get_model_url(UserFavorite, 'changelist')},
    #             {'title': '用户消息', 'url': self.get_model_url(UserMessage, 'changelist')},
    #         )},
    #
    #
    #         {'title': '系统管理', 'menus': (
    #             {'title': '用户咨询', 'url': self.get_model_url(UserAsk, 'changelist')},
    #             {'title': '首页轮播', 'url': self.get_model_url(Banner, 'changelist')},
    #             {'title': '用户分组', 'url': self.get_model_url(Group, 'changelist')},
    #             {'title': '用户权限', 'url': self.get_model_url(Permission, 'changelist')},
    #             {'title': '日志记录', 'url': self.get_model_url(Log, 'changelist')},
    #         )},
    #     )

class UserProfileAdmin(UserAdmin):
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active',  'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['code', 'email','send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields =  ['code', 'email','send_type']
    # 配置筛选字段
    list_filter =  ['code', 'email','send_type', 'send_time']
    model_icon = 'fa fa-envelope'



# 创建banner的管理类
class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']
    model_icon = 'fa fa-group'


# 将model与admin管理器进行关联注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)