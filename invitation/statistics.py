__author__ = 'User'
from invitation.models import Invitation
from invitation.export import make_couple_name


class Statistics:
    def __init__(self, invite_list=None):
        if invite_list is None:
            invite_list = Invitation.objects.all()
        self.invite_list = invite_list.order_by('-date_opened')
        self.coming = 0
        self.not_coming = 0
        self.maybe_coming = 0
        self.invite_number = 0
        self.guest_number = 0
        self.invite_rsvp = 0
        self.guest_rsvp = 0
        self.invite_opened = 0
        self.diet_list = []
        self.list_yes = []
        self.list_comments = []
        self.can_give_ride = []
        self.need_rides = []
        self.invitations_without_emails = []
        self.input_data_based_on_invites()
        self.input_rsvp_yes_list()
        self.input_ride_info()

    def input_ride_info(self):
        for invite in self.invite_list:
            for guest in invite.person_coming_list():
                if guest.needs_ride_location:
                    need_ride_guest = {"invite": invite.invitation_name,
                                       "guest": guest.name,
                                       "location": guest.needs_ride_location}
                    self.need_rides.append(need_ride_guest)
                if guest.has_car_room_location and guest.number_of_seats > 0:
                    has_ride_guest = {"invite": invite.invitation_name,
                                      "guest": guest.name,
                                      "location": guest.has_car_room_location,
                                      "seat_num": guest.number_of_seats}
                    self.can_give_ride.append(has_ride_guest)

    def input_rsvp_numbers(self, guest):
        if guest.person_rsvp == "Yes":
            self.coming += 1
            self.guest_rsvp += 1
        elif guest.person_rsvp == "No":
            if not guest.is_guest():
                self.not_coming += 1
                self.guest_rsvp += 1
        elif guest.person_rsvp == "Maybe":
            self.maybe_coming += 1
        self.guest_number += 1

    def input_diet_info(self, guest):
        if guest.diet_info:
            guest_diet = guest.diet_info
            for diet_dict in self.diet_list:
                if 'diet' in diet_dict and diet_dict['diet'] == guest_diet:
                    diet_dict['number'] += 1
                    break
            else:
                if not guest_diet == "None":
                    self.diet_list.append({
                        "diet": guest_diet,
                        "number": 1
                    })

    def input_messages(self, invite):
        if invite.personal_message:
            self.list_comments.append({"invite": invite.invitation_name,
                                       "message": invite.personal_message})

    def input_invitation_rsvp_numbers(self, invite):
        self.invite_number += 1
        if invite.has_rsvped():
            self.invite_rsvp += 1
        if invite.was_opened:
            self.invite_opened += 1

    def input_no_email(self, invite):
        has_email = False
        for guest in invite.person_list():
            if guest.email_internal_use:
                has_email = True
        if not has_email:
            self.invitations_without_emails.append(invite.invitation_name)

    def input_data_based_on_invites(self):
        for invite in self.invite_list:
            for guest in invite.person_list():
                self.input_rsvp_numbers(guest)
                self.input_diet_info(guest)
            self.input_invitation_rsvp_numbers(invite)
            self.input_messages(invite)
            self.input_no_email(invite)

    def input_rsvp_yes_list(self):
        for invite in self.invite_list:
            guest_list = invite.person_list()
            guest_number = 0
            if invite.has_guest_person() and not invite.couple:
                invite.couple = True
                invite.save()
            while guest_number < len(guest_list):
                if ((invite.couple and guest_number == 0 and len(guest_list) >= 2) and
                        guest_list[0].person_rsvp == guest_list[1].person_rsvp and
                        guest_list[0].person_rsvp in {"Yes", "No"}):
                    guest_1 = guest_list[0]
                    guest_2 = guest_list[1]
                    rsvp = guest_list[0].person_rsvp
                    and_text = " and "
                    if not invite.is_english():
                        and_text = " ו"
                    name = make_couple_name(guest_1, guest_2, and_text)
                    diet_info1 = "" if guest_1.diet_info == "None" else str(guest_1.diet_info)
                    diet_info2 = "" if guest_2.diet_info == "None" else str(guest_2.diet_info)
                    diet_info = diet_info1 + " " + diet_info2
                    guest_number += 2
                    self.list_yes.append({"invite": invite.invitation_name,
                                          "name": name,
                                          "rsvp": rsvp,
                                          "diet": diet_info})
                elif guest_list[guest_number].person_rsvp in {"Yes", "No"}:
                    guest = guest_list[guest_number]
                    if not guest.is_guest():
                        name = guest.name
                        rsvp = guest.person_rsvp
                        diet_info = "" if guest.diet_info == "None" else str(guest.diet_info)
                        self.list_yes.append({"invite": invite.invitation_name,
                                              "name": name,
                                              "rsvp": rsvp,
                                              "diet": diet_info})
                    guest_number += 1
                else:
                    guest_number += 1
                    continue

    def percent_invite_rsvped(self):
        to_return = (self.invite_rsvp/self.invite_number)*100
        to_return = "{:.1f}".format(to_return)
        return to_return

    def percent_person_rsvped(self):
        to_return = (self.guest_rsvp/self.guest_number)*100
        to_return = "{:.1f}".format(to_return)
        return to_return

    def percent_opened(self):
        to_return = (self.invite_opened/self.invite_number)*100
        to_return = "{:.1f}".format(to_return)
        return to_return

    def percent_rsvp_to_opened(self):
        to_return = (self.invite_rsvp/self.invite_opened)*100
        to_return = "{:.1f}".format(to_return)
        return to_return