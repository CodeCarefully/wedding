from django.conf.urls import patterns, include, url
from invitation import views

urlpatterns = patterns(
    '',
    url(r'^(?P<invite_id>\d+)/(?P<guest_id>\d+)/rsvp/(?P<rsvp>\w+)$', views.invitation_input_rsvp, name="rsvp"),
    url(r'^(?P<invite_id>\d+)/$', views.invitation_detail, name="detail"),
    url(r'.*', views.main_error, name="main_error"),

)
