from __future__ import unicode_literals
from django.db import models
from accounts.models import User


class Gallery(models.Model):

    image = models.ImageField(upload_to='gallery')
    description = models.CharField(max_length=100)
    uploader = models.ForeignKey(User)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name_plural = "Gallery"
