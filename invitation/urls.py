from django.conf.urls import patterns, include, url
from invitation import views

urlpatterns = patterns(
    '',
    url(r'^(?P<invite_id>\d+)/(?P<guest_id>\d+)/rsvp/(?P<rsvp>\w+)/?$', views.invitation_input_rsvp, name="rsvp"),
    url(r'^(?P<invite_id>\d+)/(?P<guest_id>\d+)/diet/(?P<diet>\w+)/?$', views.invitation_input_diet, name="diet"),
    url(r'^(?P<invite_id>\d+)/family_number/(?P<family_number>\w+)/?$', views.invitation_input_family, name="family"),
    url(r'^(?P<invite_id>\d+)/(?P<guest_id>\d+)/family_diet/?$', views.input_post_data, name="famdiet"),
    url(r'^(?P<invite_id>\d+)/(?P<lang>\w+)/?$', views.invitation_detail, name="detail"),
    url(r'^(?P<invite_id>\d+)/$', views.invitation_detail, name="detail")
)
