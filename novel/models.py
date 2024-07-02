from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    avatar = models.ImageField(upload_to="uploads/%y/%m")


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100, null=False, unique=True)
    vname = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Novel(models.Model):
    story_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="novelAvatar/%y/%m", default=None)
    description = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    total_chapter = models.IntegerField()

    def __str__(self) -> str:
        return self.story_name


class Chapter(models.Model):
    novel = models.ForeignKey(Novel, related_name="chapters", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="novelAvatar/%y/%m")
    chapter_no = models.IntegerField()
    content = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
