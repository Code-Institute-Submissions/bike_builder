from django.conf.urls import url
import views


urlpatterns = [

    url(r'^$', views.gallery, name='gallery'),
    url(r'^upload_image/$', views.upload_image, name='upload_image'),

]
