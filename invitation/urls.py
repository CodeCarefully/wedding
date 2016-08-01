from django.conf.urls import url
from invitation import views

urlpatterns = [
    url(r'^(?P<invite_id>\d+)/(?P<guest_id>\d+)/rsvp/(?P<rsvp>\w+)/?$', views.invitation_input_rsvp, name="rsvp"),
    url(r'^(?P<invite_id>\d+)/(?P<guest_id>\d+)/diet/(?P<diet>\w+)/?$', views.invitation_input_diet, name="diet"),
    url(r'^(?P<invite_id>\d+)/(?P<lang>(en|he))/?$', views.invitation_detail, name="detail"),
    url(r'^(?P<invite_id>\d+)/$', views.invitation_detail, name="detail")
]
