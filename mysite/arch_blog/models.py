import datetime

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 256)
    body = models.TextField(max_length = 4096)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    def wasPublishedRecently(self):
        return self.pub_date <= timezone.now() - datetime.timedelta(days=1)
    def hasTag(self, a_tag):
        return self.tag_set.filter(tag=a_tag).distinct().count() == 1
    def getTags(self):
        return self.tag_set.all()
    def getComments(self):
        return self.comment_set.all()
    def getAbstract(self):
        if len(self.body) < 150:
            return self.body + '...'
        else:
            return self.body[:150] + '...'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    body = models.TextField(max_length = 1024)
    author = models.CharField(max_length = 128)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.body

class Tag(models.Model):
    name = models.CharField(max_length=64)
    posts = models.ManyToManyField(Post)
    def __str__(self):
        return self.name
    
