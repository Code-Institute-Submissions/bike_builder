from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from accounts.models import User


# Create your models here.
class Gallery(models.Model):

    image = models.ImageField(upload_to='gallery')
    description = models.CharField(max_length=100)
    uploader = models.ForeignKey(User)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description
