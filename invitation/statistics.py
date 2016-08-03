__author__ = 'User'
from invitation.models import Invitation, diet_choices
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
        self.diet_choices = []
        self.list_yes = []
        self.input_data_based_on_invites()
        self.input_rsvp_yes_list()
        self.input_diet_choices()

    def input_diet_choices(self):
        for diet in diet_choices:
            self.diet_choices.append({"diet": diet[1], "number": "0"})
        for invite in self.invite_list:
            for guest in invite.person_coming_list():
                if guest.diet_choices:
                    diet_choice = guest.get_diet_choices_display()
                    for diet_dict in self.diet_choices:
                        if diet_choice == diet_dict["diet"]:
                            diet_dict["number"] = str(int(diet_dict["number"])+1)
        return

    def input_data_based_on_invites(self):
        for invite in self.invite_list:
            for guest in invite.person_list():
                if guest.is_coming():
                    self.coming += 1
                    self.guest_rsvp += 1
                elif guest.person_rsvp == "No":
                    if not guest.is_guest():
                        self.not_coming += 1
                    self.guest_rsvp += 1
                elif guest.person_rsvp == "Maybe":
                    self.maybe_coming += 1
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
            while guest_number < len(guest_list):
                if ((guest_number == 0 and len(guest_list) >= 2) and
                        guest_list[0].person_rsvp == guest_list[1].person_rsvp and
                        guest_list[0].person_rsvp in {"Yes", "No"}):
                    guest_1 = guest_list[0]
                    guest_2 = guest_list[1]
                    and_text = " and "
                    name = make_couple_name(guest_1, guest_2, and_text)
                    rsvp = guest_1.person_rsvp
                    diet = guest_1.get_diet_choices_display() + " " + guest_2.get_diet_choices_display()
                    self.list_yes.append({"invite": invite.invitation_name,
                                          "name": name,
                                          "rsvp": rsvp,
                                          "diet": diet,
                                          "id": invite.invite_id,
                                          "admin_id": invite.id,
                                          "group": invite.side + " - " + invite.group})
                    guest_number += 2
                elif guest_list[guest_number].has_rsvp() and not guest_list[guest_number].is_guest():
                    guest = guest_list[guest_number]
                    name = guest.english_name
                    rsvp = guest.person_rsvp
                    diet = guest.get_diet_choices_display()
                    self.list_yes.append({"invite": invite.invitation_name,
                                          "name": name,
                                          "rsvp": rsvp,
                                          "diet": diet})
                    guest_number += 1
                else:
                    guest_number += 1
                    continue

    def percent_invite_rsvped(self):
        if self.invite_number == 0:
            return 0
        to_return = (self.invite_rsvp/self.invite_number)*100
        to_return = "{:.1f}".format(to_return)
        return to_return

    def percent_person_rsvped(self):
        if self.guest_number == 0:
            return 0
        to_return = (self.guest_rsvp/self.guest_number)*100
        to_return = "{:.1f}".format(to_return)
        return to_return

    def percent_opened(self):
        if self.invite_number == 0:
            return 0
        to_return = (self.invite_opened/self.invite_number)*100
        to_return = "{:.1f}".format(to_return)
        return to_return

    def opened_to_rsvp_ratio(self):
        if self.invite_opened == 0:
            return 0
        to_return = (self.invite_rsvp/self.invite_opened)*100
        to_return = "{:.1f}".format(to_return)
        return to_return