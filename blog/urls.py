from django.conf.urls import url

from . import views
#从当前文件夹导入，用 . 表示

#网址和处理视图函数的关系
#app_name = 'blog'

urlpatterns = [
    #主页
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),
    url(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivesView.as_view(),name='archives'),
    #url(r'category/(?P<pk>[0-9]/$',views.category,name='category'),
    #url(r'category/(?P<pk>[0-9])/$',views.catetory,name='category')
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
]
