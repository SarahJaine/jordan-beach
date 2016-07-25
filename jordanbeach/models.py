from django.db import models


class Teaching(models.Model):
    role_choices = (
        ('instructor', 'Instructor'),
        ('mentor', 'Mentor'),
        )
    role = models.CharField(max_length=20, choices=role_choices)
    year_start = models.PositiveSmallIntegerField()
    year_end = models.PositiveSmallIntegerField(null=True, blank=True)
    course_name = models.CharField(max_length=200, null=True, blank=True)
    course_venue = models.CharField(max_length=200, null=True, blank=True)
    mentee = models.CharField(max_length=200, null=True, blank=True)
    mentee_role = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.role


class Award(models.Model):
    name = models.CharField(max_length=200)
    source = models.CharField(max_length=200, null=True)
    date = models.DateField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name


class Poster(models.Model):
    authors = models.CharField(max_length=400)
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=400)
    date = models.DateField()
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=2, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


class Talk(models.Model):
    title = models.CharField(max_length=200)
    event = models.CharField(max_length=200, null=True)
    venue = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=2, null=True)
    date = models.DateField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    authors = models.CharField(max_length=400, null=True)
    journal_name = models.CharField(max_length=100)
    journal_vol = models.PositiveSmallIntegerField(null=True, blank=True)
    journal_issue = models.PositiveSmallIntegerField(null=True, blank=True)
    date = models.DateField(null=True)
    pages = models.CharField(max_length=20, null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title
