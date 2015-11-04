# coding=utf-8
__author__ = 'chenpengpeng'

from .models import Event
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.extras.widgets import SelectDateWidget
from OnlineBug import settings
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
class EventForm(forms.Form):
    STATUS_CHOICES = (
        ("create", "新建"),
        ("review", "审核"),
        ("assigned", "已分派(技术部)"),
        ("resolved", "已解决"),
        ("closed", "关闭"),
        ("duplicated", "重复的"),
    )
    BUSINESS_CHOICES = (
        ("student", "家长端"),
        ("teacher", "老师端"),
        ("admin", "运营端"),
        ("ta", "助教端"),
        ("third_place", "第三方场地")
    )
    PLATFORM_CHOICES = (
        ("ios", "IOS"),
        ("android", "安卓"),
        ("web", "WEB")
    )
    title = forms.CharField(label=u"标题")
    content = forms.CharField(
        label="描述",
        widget=forms.Textarea())
    comments = forms.CharField(
        label="注释",
        widget=forms.Textarea(),
    )
    version = forms.FloatField(label=u"版本")
    business_type = forms.CharField(label=u"业务类型")
    platform = forms.CharField(label=u"客户端")
    status = forms.CharField(label=u"状态")

    level = forms.CharField(label=u"严重等级",)
    emergency = forms.CharField(label=u"紧急程度",)
    channel = forms.CharField(label=u"来源")
    solution = forms.CharField(label=u"解决方案")
   # expect_resolve_time = forms.DateField(label="预计解决时间",widget=AdminDateWidget,required=False)
    expect_resolve_time = DateTimeWidget( usel10n=True, bootstrap_version=3)
    #reporter = forms.Form(User)
    # op_history=models.ForeignKey(EventLog)
   # attachment = forms.FileField(label=u"附件")
    comments = forms.CharField(
        label="注释",
        widget=forms.Textarea(),
        required=False
    )
    def save(self, user):
        data = self.cleaned_data
        for key in data.iteritems():
           print(key,data.get(key))

        bug = Event(
            title = data["title"],
            content = data["content"],
            version = data["version"],
            business_type = data["business_type"],
            platform = data["platform"],
            status = data["status"],
            comments = data["comments"],
            level =data["level"],
            solution=data["solution"],
            emergency =data["emergency"],
            channel = data["channel"],
           # expect_resolve_time = data["expect_resolve_time"],
            reporter=user,
            #attachment = data["attachment"]
        )
        bug.save()
