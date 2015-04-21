from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from invitation.models import Invitation, Person
from django.utils import timezone
from invitation.export import export_all_info, EXPORT_ALL_INFO_NAME
import re


def get_pk_from_id(invite_id):
    all_invitations = Invitation.objects.all()
    for invite in all_invitations:
        if invite.invite_id == invite_id:
            return invite.pk
    return 0


def invitation_detail(request, invite_id, lang=None):
    pk = get_pk_from_id(invite_id)
    try:
        invitation = Invitation.objects.get(pk=pk)
    except:
        return render(request, 'invitation/main.html', {'error': 'true'})
    invitation.was_opened = True
    invitation.date_opened = timezone.now()
    invitation.save()
    if not lang:
        if invitation.language == "English":
            return HttpResponseRedirect("en")
        else:
            return HttpResponseRedirect("he")
    return render(request, 'invitation/main.html', {'invitation': invitation, 'language': lang})


def main(request):
    return render(request, 'invitation/main.html')


def error_page(request):
    return render(request, 'invitation/404.html')


def invitation_input_rsvp(request, invite_id, guest_id, rsvp):
    guest_pk = guest_id
    guest = get_object_or_404(Person, pk=guest_pk)
    guest.person_rsvp = rsvp
    guest.save()
    invite = guest.invitation
    if invite.has_guest_person():
        reg_rsvp = "Maybe"
        for person in invite.person_list():
            if person.is_guest():
                guest_rsvp = person.person_rsvp
                if ((reg_rsvp == "No" and not guest_rsvp == "No") or
                        (reg_rsvp == "Maybe" and guest_rsvp == "Yes")):
                    person.person_rsvp = reg_rsvp
                    person.save()
            else:
                reg_rsvp = person.person_rsvp
    return HttpResponse('')


def export_all(request):
    all_invitations = Invitation.objects.all()
    export_all_info(all_invitations)
    output = open(EXPORT_ALL_INFO_NAME, "rb")
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=All_info.xlsx"
    return response
