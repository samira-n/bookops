from django.db import models

from categories.models import Category


class Article(models.Model):
    title = models.CharField(max_length=250, null=True)
    text = models.TextField(null=True)
    datetime = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
