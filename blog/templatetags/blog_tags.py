#导入post模块
from ..models import Post,Category
from django import template #导入模版使用模块

from django.db.models.aggregates import Count #导入计数

register = template.Library()

#定义一个函数来获取最新文章
@register.simple_tag #装饰成一个模版标签
def get_recent_posts(num=5): #获取多少篇最新文章
    #返回最新文章
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives(): #归档
    #返回最新文章
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories(): # 得到分类
    #返回最新文章
    return Category.objects.annotate(num_posts=Count("post")).filter(num_posts__gt=0)