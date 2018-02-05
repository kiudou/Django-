from django.db import models

# Create your models here.
class Article(models.Model): #博客
    title = models.CharField(max_length=120) #标题
    category = models.CharField(max_length=100, blank=True) #标签
    time = models.DateTimeField(auto_now_add=True) #日期,auto_now_add自动设置对象增加时间
    content = models.TextField(blank=True, null=True) #正文

    def __unicode__(self): #使用title来表示自己
        return self.title
    class Meta: #时间下降排序
        ordering = ['-time']