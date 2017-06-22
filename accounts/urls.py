from django.conf.urls import url
import views


urlpatterns = [

    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/edit_profile/$', views.edit_profile, name='edit_profile'),

]
