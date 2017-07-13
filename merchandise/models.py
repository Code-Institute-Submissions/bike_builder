from __future__ import unicode_literals
from django.db import models


class Merchandise(models.Model):

    image = models.ImageField(upload_to="merch_images", blank=True, null=True)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Merchandise"
