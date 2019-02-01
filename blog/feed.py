from django.contrib.syndication.views import Feed
from .models import Post

class AllPostRssFeed(Feed):
    #显示在rss阅读器上的标题
    title = '欢迎订阅我的博客'

    #通过rss跳转到网站的地址
    link = '/'

    #
    description ='django 博客教程演示项目测试文件'

    #需要显示的条目内容
    def item(self):
        return Post.objects.all()

    #rss中显示的标题
    def item_title(self,item):
        return '[%s] %s' % (item.category,item.title)

    def item_description(self,item):
        return item.body
