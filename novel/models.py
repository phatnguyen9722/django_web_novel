from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    """
    This class is used for Custom User
    """

    avatar = models.ImageField(upload_to="uploads/%y/%m", blank=True, null=True)


class Category(models.Model):
    """
    This class is used for Category
    """

    class Meta:
        """
        Customize your Category
        """

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
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    image = models.ImageField(
        upload_to="novelAvatar/%y/%m", default=None, blank=True, null=True
    )
    description = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    total_chapter = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Chapter(models.Model):
    novel = models.ForeignKey(Novel, related_name="chapters", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to="novelAvatar/%y/%m", default=None, blank=True, null=True
    )
    chapter_no = models.IntegerField()
    content = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.novel.title} - Chapter {self.chapter_no}: {self.title}"
