from django.conf.urls import patterns, include, url
from invitation import views

urlpatterns = patterns(
    '',
    url(r'^(?P<invite_id>\d+)/$', views.invitation_detail, name="detail")
#    url(r'^(?P<invite_id>\d+)/complete/$', views.InvitationCompleteView.as_view(), name="complete")
)
