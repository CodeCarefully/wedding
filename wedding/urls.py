from django.conf.urls import include, url
from invitation.admin import site
from invitation import views
from django.contrib import admin
from adminplus.sites import AdminSitePlus

admin.autodiscover()

urlpatterns = [
    url(r'^invitation/', include("invitation.urls", namespace="invitations")),
    url(r'^admin/', include(site.urls)),
    url(r'^export_all$', views.export_all, name="all_export"),
    url(r'^import_from_local_excel$', views.import_from_excel_view, name="excel_import"),
    url(r'^(?P<lang>(en|he))/?$', views.main_without_code, name="without_code"),
    url(r'^.*/$', views.main_without_code, name="without_code"),
    url(r'^$', views.main_without_code, name="without_code"),
]
