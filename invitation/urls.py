from django.conf.urls import patterns, include, url
from invitation import views

urlpatterns = patterns(
    '',
    url(r'^(?P<invite_id>\d+)/(?P<guest_id>\d+)/rsvp_detail/?$', views.input_detail, name="invite_input"),
    url(r'^(?P<invite_id>\d+)/message/?$', views.input_message, name="message"),
    url(r'^(?P<invite_id>\d+)/(?P<guest_id>\d+)/rsvp/(?P<rsvp>\w+)/?$', views.invitation_input_rsvp, name="rsvp"),
    url(r'^(?P<invite_id>\d+)/$', views.invitation_detail, name="detail"),
    url(r'$', views.main_error, name="main_error"),
    url(r'.*/', views.main_error, name="main_error"),
)
