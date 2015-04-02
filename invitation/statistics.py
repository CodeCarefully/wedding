__author__ = 'User'
from invitation.models import Invitation


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
        self.vegans_coming = 0
        self.list_yes = []
        self.list_comments = []
        for invite in self.invite_list:
            for guest in invite.person_list():
                if guest.person_rsvp == "Yes":
                    if guest.is_vegan:
                        self.vegans_coming += 1
                    self.coming += 1
                    self.guest_rsvp += 1
                    self.list_yes.append({"invite": invite.invitation_name,
                                          "person": guest.name})
                elif guest.person_rsvp == "No":
                    self.not_coming += 1
                    self.guest_rsvp += 1
                elif guest.person_rsvp == "Maybe":
                    self.maybe_coming += 1
                self.guest_number += 1
            self.invite_number += 1
            if invite.has_rsvped():
                self.invite_rsvp += 1
            if invite.was_opened:
                self.invite_opened += 1
            if invite.personal_message:
                self.list_comments.append({"invite": invite.invitation_name,
                                           "comment": invite.personal_message})

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

