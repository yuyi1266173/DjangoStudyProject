from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    """板块"""

    # unique=True : 强制数据库级别字段的唯⼀性
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    """主题"""

    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    # 外键关联   related_name='topics'表示board.topics可以查看该板块下所有的相关主题
    # related_name默认为(class_name)_set --> topic_set
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')


class Post(models.Model):
    """帖子/评论"""

    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    # related_name='+' 指示Django我们不需要这种反向关系，所以它会被忽略
    updated_by = models.ForeignKey(User, null=True, related_name='+')


