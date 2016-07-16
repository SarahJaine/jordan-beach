from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    journal_name = models.CharField(max_length=255)
    journal_vol = models.IntegerField(null=True)
    journal_issue = models.IntegerField(null=True)
    date = models.DateField(null=True)
    link = models.URLField(null=True)

    class Meta:
        ordering = ["title"]
