from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Manufacturers(models.Model):
    manufacturer = models.CharField(max_length=60)

    def __unicode__(self):
        return self.manufacturer


class Layouts(models.Model):
    layout = models.CharField(max_length=60)

    def __unicode__(self):
        return self.layout


class Bikes(models.Model):
    manufacturer = models.ForeignKey(Manufacturers)
    model = models.CharField(max_length=60)
    cylinders = models.PositiveSmallIntegerField()
    layout = models.ForeignKey(Layouts)

    def __unicode__(self):
        return self.model
