from django.db import models

# Create your models here.
class Comment(models.Model):
    #必须继承models.Model这个类

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField() #用户发表的内容

    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)

    #在新的Django中必须加入on_delete这个参数

    def __str__(self):
        return self.text[:20]
