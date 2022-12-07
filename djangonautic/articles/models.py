from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# For More Condition
# https://docs.djangoproject.com/en/4.1/topics/db/models/
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in tumbnail later
    thumb = models.ImageField(default='default.png', blank=True)
    # add in author later
    author = models.ForeignKey(User,on_delete=models.PROTECT,default=None)

    #to Control how article look in shell
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'