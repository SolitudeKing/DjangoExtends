from datetime import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class BaseModel(models.Model):
    """ 基础model """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_deleted = models.BooleanField(default=False, verbose_name="是否删除")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="删除时间")

    class Meta:
        abstract = True  # 抽象模型类，用于继承，不会创建表

# 创建保存前的信号，当模型删除时自动设置删除时间，当模型恢复时自动取消删除时间


@receiver(pre_save, sender=BaseModel)
def preSaveHandler(sender, instance: BaseModel, **kwargs):
    if instance.is_deleted:
        instance.deleted_at = datetime.now()
    else:
        instance.deleted_at = None
        instance.created_at = datetime.now()
        instance.save()
