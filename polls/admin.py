from django.contrib import admin
from .models import Poll, PollSubject, Vote


admin.site.register(Poll)
admin.site.register(PollSubject)
admin.site.register(Vote)
