from django.conf.urls import url
import views


urlpatterns = [

    url(r'^$', views.how_to_guides, name='how_to_guides'),
    url(r'^upload_guide/$', views.upload_guide, name='upload_guide'),

]
