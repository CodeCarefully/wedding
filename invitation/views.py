from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from invitation.models import Invitation, Person
from django.utils import timezone
import re


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
    return render(request, 'invitation/main.html')


def main_error(request):
    return render(request, 'invitation/main.html', {'error': 'true'})


def thankyou(request):
    return render(request, 'invitation/thankyou.html')


def invitation_input_rsvp(request, invite_id, guest_id, rsvp):
    guest_pk = guest_id
    guest = get_object_or_404(Person, pk=guest_pk)
    guest.person_rsvp = rsvp
    guest.save()
    return HttpResponse('')


def input_detail(request, invite_id, guest_id):
    post_info = request.POST
    guest_pk = guest_id
    guest = get_object_or_404(Person, pk=guest_pk)
    if "isVegan" in post_info and is_bool(post_info["isVegan"]):
        is_vegan = pars_bool(post_info["isVegan"])
        guest.is_vegan = is_vegan
    if "dietaryInfo" in post_info:
        guest.diet_info = post_info["dietaryInfo"]
    if "needRideLocation" in post_info:
        guest.needs_ride_location = post_info["needRideLocation"]
    if "giveRideLocation" in post_info:
        guest.has_car_room_location = post_info["giveRideLocation"]
    if "numSeats" in post_info:
        if is_int(post_info["numSeats"]):
            number_of_seats = int(post_info["numSeats"])
            guest.number_of_seats = number_of_seats
        else:
            pass  # TODO
    if "email" in post_info:
        if is_email(post_info["email"]):
            guest.email_app = post_info["email"]
        else:
            pass  # TODO
    if "phone" in post_info:
        if is_phone_number(post_info["phone"]):
            guest.phone_app = post_info["phone"]
        else:
            pass  # TODO
    guest.save()
    return HttpResponse('')


def input_message(request, invite_id):
    post_info = request.POST
    invite_pk = get_pk_from_id(invite_id)
    invite = get_object_or_404(Invitation, pk=invite_pk)
    if "message" in post_info:
        invite.personal_message = post_info["message"]
    invite.save()
    return HttpResponse('')


def is_phone_number(_input):
    _input = re.sub("[()\. -]", '', _input)
    return is_int(_input) and len(_input) == 10


def is_int(_input):
    try:
        int(_input)
        return True
    except ValueError:
        return False


def is_email(_input):
    return re.match(r"[^@]+@[^@]+\.[^@]+", _input)


def is_bool(_input):
    if _input in {"True", 1, "1", "False", 0, "0"}:
        return True
    else:
        return False


def pars_bool(_input):
    if _input in {"True", 1, "1"}:
        return True
    elif _input in {"False", 0, "0"}:
        return False
    else:
        raise ValueError("Input not boolean")


# TODO
# def statistics(request):
#     all_invitations = Invitation.objects.all()
#     total_opened = 0
#     total_invited = 0
#     total_coming = 0
#     total_veg = 0
#     for invitation in all_invitations:



