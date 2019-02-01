from django.conf.urls import url

from . import views
#从当前文件夹导入，用 . 表示

#网址和处理视图函数的关系
app_name='comments'
urlpatterns = [
    #主页
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]