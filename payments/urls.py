from django.conf.urls import url
import views


urlpatterns = [

    url(r'^(?P<product_id>\d+)/$', views.place_order, name='place_order'),

]
