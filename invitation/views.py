from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from invitation.models import Invitation, Person
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
import xlsxwriter
from invitation.export import export_to_excel


def get_pk_from_id(invite_id):
    all_invitations = Invitation.objects.all()
    for invite in all_invitations:
        if invite.invite_id == invite_id:
            return invite.pk
    return 0


def invitation_detail(request, invite_id):
    pk = get_pk_from_id(invite_id)
    try:
        invitation = Invitation.objects.get(pk=pk)
    except:
        return render(request, 'invitation/main.html', {'error': 'true'})
    invitation.was_opened = True
    invitation.date_opened = timezone.now()
    invitation.save()
    return render(request, 'invitation/main.html', {'invitation': invitation})


def main(request):
    all_invitations = Invitation.objects.all()
    export_to_excel(all_invitations)
    return render(request, 'invitation/main.html')


def thankyou(request):
    return render(request, 'invitation/thankyou.html')


def invitation_input_rsvp(request, invitation_id, guest_id, rsvp):
    guest_pk = guest_id
    guest = get_object_or_404(Person, pk=guest_pk)
    guest.person_rsvp = rsvp
    guest.save()

# TODO
# def statistics(request):
#     all_invitations = Invitation.objects.all()
#     total_opened = 0
#     total_invited = 0
#     total_coming = 0
#     total_veg = 0
#     for invitation in all_invitations:



