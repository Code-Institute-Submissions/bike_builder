"""bike_builder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Home
    url(r'', include('home.urls')),

    # Media URL for images
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # Accounts
    url(r'^accounts/', include('accounts.urls')),

    # Forum
    url(r'^forum/', include('threads.urls')),

    # Poll
    url(r'^thread/', include('polls.urls')),

    # Gallery
    url(r'^gallery/', include('gallery.urls')),

    # How to guides
    url(r'^how_to_guides/', include('how_to_guides.urls')),

    # Merchandise
    url(r'^merchandise/', include('merchandise.urls')),

    # Payments
    url(r'^place_order/', include('payments.urls')),

    #  Bike Selector
    url(r'^bike_selector/', include('bike_selector.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
