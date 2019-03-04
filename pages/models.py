from django.db import models

# Create your models here.
from django.utils import timezone

class Article(models.Model):
    '''文章'''
    title = models.CharField('标题', max_length=200) # 标题
    content = models.TextField() # 内容
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    upate_time = models.DateTimeField('最后修改时间', auto_now=True)
    tags = models.ManyToManyField('Tag', through='ArticleTags')

    def __str__(self):
        return self.title 

class Tag(models.Model):
    '''标签'''
    name = models.CharField('标签名', max_length=30) #标签名
    articles = models.ManyToManyField('Article', through='ArticleTags')

    def __str__(self):
        return self.name 

class ArticleTags(models.Model):
    '''文章-标签关联'''
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 文章id
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE) # 标签id

    def __str__(self):
        return '{0}[{1}]'.format(self.article.title, self.tag.name)