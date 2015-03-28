from django.conf.urls import patterns, include, url
from django.contrib import admin
from invitation.admin import site
from invitation import views

urlpatterns = patterns(
    '',
    url(r'^invitation/', include("invitation.urls", namespace="invitations")),
    url(r'^admin/', include(site.urls)),
    url(r'^$', views.main, name="main"),
    url(r'^thankyou.html$', views.thankyou, name="thankyou")
)
