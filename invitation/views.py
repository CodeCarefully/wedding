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


def invitation_detail(request, invite_id):
    pk = get_pk_from_id(invite_id)
    invitation = get_object_or_404(Invitation, pk=pk)
    invitation.was_opened = True
    invitation.date_opened = timezone.now()
    invitation.save()
    return render(request, 'invitation/main.html', {'invitation': invitation})


def main(request):
    return render(request, 'invitation/main.html')


def thankyou(request):
    return render(request, 'invitation/thankyou.html')


def invitation_input_family_rsvp(request, invite_id, family_rsvp):
    invite_pk = get_pk_from_id(invite_id)
    invitation = get_object_or_404(Invitation, pk=invite_pk)
    invitation.guest_rsvp = family_rsvp
    invitation.save()

# TODO
# def statistics(request):
#     all_invitations = Invitation.objects.all()
#     total_opened = 0
#     total_invited = 0
#     total_coming = 0
#     total_veg = 0
#     for invitation in all_invitations:


