from django.conf.urls import patterns, include, url
from django.contrib import admin
from invitation.admin import site

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'wedding.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(site.urls)),
)
