from django.db import models
from slugify import Slugify


class Direction(models.Model):
    direction = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    sort_number = models.IntegerField()

    class Meta:
        ordering = ["sort_number"]

    def save(self, *args, **kwargs):
        my_slugify = Slugify()
        if self.slug:
            super(Direction, self).save(*args, **kwargs)
        else:
            self.slug = my_slugify(self.direction, to_lower=True)
            super(Direction, self).save(*args, **kwargs)

    def __str__(self):
        return self.direction


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    directions = models.ManyToManyField(Direction)
    description = models.TextField()
    work_experience = models.IntegerField()
    date_birth = models.DateField()
    sort_number = models.IntegerField()

    class Meta:
        ordering = ["sort_number"]

    def save(self, *args, **kwargs):
        my_slugify = Slugify()
        if self.slug:
            super(Doctor, self).save(*args, **kwargs)
        else:
            self.slug = my_slugify(self.last_name, to_lower=True)
            super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
