# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from OnlineBug import settings
import datetime
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class EventLog(models.Model):
    id = models.AutoField(unique=False,primary_key=True)
    event_id = models.IntegerField("问题编号")
    operation = models.CharField("操作",max_length=120)
    op_user = models.ManyToManyField(User)
    op_time = models.DateTimeField(auto_now_add=True)

# Create your models here.
class Event(models.Model):
    def __str__(self):
        return self.title

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
    title = models.CharField("标题", max_length=120)
    content = models.TextField("问题详情", )
    version = models.FloatField("版本")
    business_type = models.CharField("业务类型", choices=BUSINESS_CHOICES, max_length=120)
    platform = models.CharField("客户端", choices=PLATFORM_CHOICES, max_length=120)
    status = models.CharField("状态", choices=STATUS_CHOICES, max_length=120)
    create_time = models.DateTimeField("提交时间", auto_created=True, default=timezone.now,editable=False)
    comments = models.TextField("备注", blank=True)
    last_update_time = models.DateTimeField("最后更新时间", auto_now_add=True)
    level = models.CharField("严重等级", max_length=100)
    solution = models.CharField("解决方案", max_length=100)
    expect_resolve_time = models.DateField("预计解决时间",blank=True)
    emergency = models.CharField("紧急程度", max_length=100)
    channel = models.CharField("来源",max_length=100,blank=True)
    reporter = models.ForeignKey(User)
    #op_history=models.ForeignKey(EventLog)
    attachment = models.FileField("附件",upload_to=settings.MEDIA_ROOT)


