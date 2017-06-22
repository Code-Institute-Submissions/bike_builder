from django.conf.urls import url
import views


urlpatterns = [

    url(r'^$', views.bike_search, name='bike_search'),

]
