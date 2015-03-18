from django.conf.urls import patterns, include, url
from django.contrib import admin
from invitation.admin import site

urlpatterns = patterns(
    '',
    url(r'^invitation/', include("invitation.urls", namespace="invitations")),
    url(r'^admin/', include(site.urls)),
)
