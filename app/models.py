from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("タイトル", max_length=20)
    content = models.TextField("本文", max_length=200)
    created = models.DateTimeField("作成日", default=timezone.now)
    
    read = models.IntegerField(null=True, blank=True , default = 1)
    readtext = models.TextField(null=True, blank=True , default= 'a')

    def __str__(self):
        return self.title
    