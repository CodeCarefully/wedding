from django.conf.urls import patterns, include, url
from invitation import views

urlpatterns = patterns(
    '',
    url(r'^(?P<invite_id>\d+)/family_rsvp/(?P<guest_rsvp>\w+)$', views.invitation_input_family_rsvp, name="family_rsvp"),
    url(r'^(?P<invite_id>\d+)/$', views.invitation_detail, name="detail"),

)
