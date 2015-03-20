from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from invitation.models import Invitation, Person
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


def get_pk_from_id(invite_id):
    all_invitations = Invitation.objects.all()
    for invite in all_invitations:
        if invite.invite_id == invite_id:
            return invite.pk
    return 0


# class InvitationDetailView(generic.DetailView):
#     model = Invitation
#     template_name = "invitation/detail.html"
#
#
# class InvitationCompleteView(generic.DetailView):
#     model = Invitation
#     template_name = "invitation/complete.html"


def invitation_detail(request, invite_id):
    pk = get_pk_from_id(invite_id)
    invitation = get_object_or_404(Invitation, pk=pk)
    invitation.was_opened = True
    invitation.date_opened = timezone.now()
    return render(request, 'invitation/detail.html', {'invitation': invitation})


def invitation_input_guest_RSVP(request, invite_id, guest_RSVP):
    invite_pk = get_pk_from_id(invite_id)
    invitation = get_object_or_404(Invitation, pk=invite_pk)
    invitation.guest_RSVP = guest_RSVP

