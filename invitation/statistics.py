__author__ = 'User'
from invitation.models import Invitation
from invitation.export import make_couple_name


class Statistics:
    def __init__(self, invite_list=None):
        if invite_list is None:
            invite_list = Invitation.objects.all()
        self.invite_list = invite_list.order_by('date_opened')
        self.coming = 0
        self.not_coming = 0
        self.maybe_coming = 0
        self.invite_number = 0
        self.guest_number = 0
        self.invite_rsvp = 0
        self.guest_rsvp = 0
        self.invite_opened = 0
        self.diet_choices = {"Other": []}
        self.list_yes = []
        self.input_data_based_on_invites()
        self.input_rsvp_yes_list()
        self.input_diet_choices()

    def input_diet_choices(self):
        for invite in self.invite_list:
            for guest in invite.person_list():
                if guest.diet_choices:
                    if guest.diet_choices in self.diet_choices:
                        self.diet_choices[guest.diet_choices] += 1
                    else:
                        self.diet_choices[guest.diet_choices] = 1
                if guest.diet_blank:
                    to_insert = {"invite": invite.invitation_name,
                                 "name": guest.english_name,
                                 "dietinfo": guest.diet_blank}
                    self.diet_choices["Other"].append(to_insert)

    def input_data_based_on_invites(self):
        for invite in self.invite_list:
            if not invite.is_family:
                for guest in invite.person_list():
                    if guest.person_rsvp == "Yes":
                        self.coming += 1
                        self.guest_rsvp += 1
                    elif guest.person_rsvp == "No":
                        self.not_coming += 1
                        self.guest_rsvp += 1
                    elif guest.person_rsvp == "Maybe":
                        self.maybe_coming += 1
            else:  # family invite
                family_rsvp = invite.get_family_rsvp()
                if family_rsvp == "Yes":
                    self.coming += invite.family_rsvp_number
                    self.guest_rsvp += invite.family_size
                    self.not_coming += invite.family_size - invite.family_rsvp_number
                elif family_rsvp == "No":
                    self.not_coming += invite.family_size
                    self.guest_rsvp += invite.family_size
                elif family_rsvp == "Maybe":
                    self.maybe_coming += invite.family_size
            self.guest_number += invite.invitation_total_invited()
            self.invite_number += 1
            if invite.has_rsvped():
                self.invite_rsvp += 1
            if invite.was_opened:
                self.invite_opened += 1

    def input_rsvp_yes_list(self):
        for invite in self.invite_list:
            guest_list = invite.person_list()
            guest_number = 0
            if invite.is_family and invite.get_family_rsvp() == "Yes":
                name = guest_list[0].english_name + " [{}/{}]".format(invite.family_rsvp_number, invite.family_size)
                self.list_yes.append({"invite": invite.invitation_name,
                                      "name": name})
                continue
            while guest_number < len(guest_list):
                if ((guest_number == 0 and len(guest_list) >= 2) and
                        guest_list[0].person_rsvp == "Yes" and guest_list[1].person_rsvp == "Yes"):
                    guest_1 = guest_list[0]
                    guest_2 = guest_list[1]
                    and_text = " and "
                    name = make_couple_name(guest_1, guest_2, and_text)
                    guest_number += 2
                    self.list_yes.append({"invite": invite.invitation_name,
                                          "name": name})
                elif guest_list[guest_number].person_rsvp == "Yes":
                    guest = guest_list[guest_number]
                    name = guest.english_name
                    guest_number += 1
                    self.list_yes.append({"invite": invite.invitation_name,
                                          "name": name})
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