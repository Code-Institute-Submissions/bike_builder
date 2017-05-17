from __future__ import unicode_literals
from django.db import models
from accounts.models import User


# Create your models here.
class HowTo(models.Model):

    description = models.CharField(max_length=250)
    url = models.URLField()
    uploader = models.ForeignKey(User)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.url
