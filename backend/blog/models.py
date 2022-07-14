import re
from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="blog/post/%Y/%m/%d")
    content = models.TextField()
    tag_set = models.ManyToManyField("Tag", blank=True)
    category_set = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def extract_tag_list(self):
        tag_name_list = re.findall(r"#([a-zA-Z\dㄱ-힣]+)", self.content)
        tag_list = []
        for tag_name in tag_name_list:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)
        return tag_list

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.pk])

    def is_like_user(self, user):
        return self.like_user_set.filter(pk=user.pk).exists()

    class Meta:
        ordering = ["-id"]

class Tag(TimestampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(TimestampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name