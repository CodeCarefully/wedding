from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from invitation.models import Invitation, Person
from django.utils import timezone


def get_pk_from_id(invite_id):
    all_invitations = Invitation.objects.all()
    for invite in all_invitations:
        if invite.invite_id == invite_id:
            return invite.pk
    return 0


@csrf_exempt
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
    return render(request, 'invitation/main.html')


def main_error(request):
    return render(request, 'invitation/main.html', {'error': 'true'})


def thankyou(request):
    return render(request, 'invitation/thankyou.html')


@csrf_exempt
def invitation_input_rsvp(request, invite_id, guest_id, rsvp):
    guest_pk = guest_id
    guest = get_object_or_404(Person, pk=guest_pk)
    guest.person_rsvp = rsvp
    guest.save()
    return HttpResponse('')

# TODO
# def statistics(request):
#     all_invitations = Invitation.objects.all()
#     total_opened = 0
#     total_invited = 0
#     total_coming = 0
#     total_veg = 0
#     for invitation in all_invitations:



