from django.db import models
from accounts.models import User


CHOICES = [

    (1, "公開中"),(0, '非公開'),

]


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_for_pro = models.BooleanField(default=False)
    is_public = models.IntegerField(default=0, choices=CHOICES)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
