from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings


class Subject(models.Model):

    name = models.CharField(max_length=255)
    description = HTMLField()
    icon = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def latest_post_thread_id(self):

        def latest_thread_date(t):
            return t.posts.all().order_by('-created_at')[0].created_at

        thread_list = list(self.threads.all())
        thread_list.sort(reverse=True, key=latest_thread_date)
        return thread_list[0].id


class Thread(models.Model):

    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)  # record how often a thread is viewed

    def __unicode__(self):
        return self.name


class Post(models.Model):

    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='forum_images', blank=True, null=True)

    def __unicode__(self):
        return self.comment[:100]
