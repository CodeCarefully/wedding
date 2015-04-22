from django.conf.urls import patterns, include, url
from invitation.admin import site
from invitation import views
from django.contrib import admin
from adminplus.sites import AdminSitePlus

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^invitation/', include("invitation.urls", namespace="invitations")),
    url(r'^admin/', include(site.urls)),
    url(r'^$', views.main, name="main"),
    url(r'^thankyou.html$', views.thankyou, name="thankyou"),
    url(r'^export_all$', views.export_all, name="all_export"),
    url(r'^export_hall$', views.export_hall_app, name="hall_app_export"),
    url(r'^export_rides$', views.export_rides_view, name="rides_export"),
    url(r'^', views.main, name="main")
)
