from __future__ import unicode_literals
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Layout(models.Model):
    layout = models.CharField(max_length=60)

    def __unicode__(self):
        return self.layout


class Bike(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    model = models.CharField(max_length=60)
    cylinders = models.PositiveSmallIntegerField()
    layout = models.ForeignKey(Layout)

    def __unicode__(self):
        return self.model
