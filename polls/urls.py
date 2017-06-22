from django.conf.urls import url
from threads import views as forum_views


urlpatterns = [

    url(r'^vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),

]
