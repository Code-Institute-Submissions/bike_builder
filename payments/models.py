from __future__ import unicode_literals
from django.db import models
# from django.conf import settings
from merchandise.models import Merchandise


# Create your models here.
class Purchase(models.Model):

    item = models.ForeignKey(Merchandise)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    address_line_1 = models.CharField(max_length=60)
    address_line_2 = models.CharField(max_length=60)
    address_line_3 = models.CharField(max_length=60)
    address_line_4 = models.CharField(max_length=60)
    post_code = models.CharField(max_length=12)
    email_address = models.EmailField()
    stripe_id = models.CharField(max_length=40, default='')
