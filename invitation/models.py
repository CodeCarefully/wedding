from django.db import models
from django.utils import timezone
from random import randint


class BaseModel(models.Model):
    # created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, default=timezone.now())

    class Meta:
        abstract = True


# class RSVPState():
#     yes = "Yes"
#     maybe = "Maybe"
#     no = "No"


RSVP_choices = [('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')]
side_choices = [('Bride', 'Bride'), ('Groom', 'Groom'), ('Both', 'Both')]
group_choices = [
    ('Bride Friends', 'Bride Friends'),
    ('Bride Family', 'Bride Family'),
    ('Groom Friends', 'Groom Friends'),
    ('Groom Family', 'Groom Family'),
]


def is_id_good(invite_id):
    all_invitations = Invitation.objects.all()
    for id in [invite.invite_id for invite in all_invitations]:
        if id == invite_id:
            return False
    return True


def id_generator():
    invite_id = randint(1, 99999)
    good_id = is_id_good(invite_id)
    while not good_id:
        invite_id = randint(1, 99999)
        good_id = is_id_good(invite_id)
    return invite_id


class Invitation(BaseModel):
    invite_id = models.SlugField(editable=False, unique=True, default=id_generator)
    with_guest = models.BooleanField(default=False)
    family_size = models.IntegerField(default=0)
    guest_RSVP = models.CharField(max_length=200, choices=RSVP_choices, default='Maybe')
    family_RSVP = models.CharField(max_length=200, choices=RSVP_choices, default='Maybe')
    family_RSVP_number = models.IntegerField(default=0)
    personal_message = models.TextField(max_length=400, default="", blank=True)
    invitation_name = models.CharField(max_length=200, default="", blank=True)
    date_opened = models.DateTimeField(default=timezone.datetime(2000, 1, 1))
    was_opened = models.BooleanField(default=False)
    side = models.CharField(max_length=200, choices=side_choices, default='Both')
    group = models.CharField(max_length=200, choices=group_choices, blank=True)

    def invitation_type(self):
        if self.with_guest:
            return "Guest"
        elif self.family_size > 0:
            return "Family"
        else:
            return "People"

    def invitation_total_RSVP(self):
        total_rsvp = 0
        if self.family_size and self.family_RSVP == "Yes":
            return self.family_RSVP_number
        elif self.with_guest and self.guest_RSVP == "Yes":
            total_rsvp += 1
        people = Person.objects.filter(invitation=self.id)
        for person in people:
            if person.person_RSVP == "Yes":
                total_rsvp += 1
        return total_rsvp

    def __str__(self):
        return str(self.id)

    # TODO LATER
    # def invitation_size(self):
    #     size = 0
    #     size += self.family_size
    #     if self.with_guest:
    #         size += 1
    #     return size


class Person(BaseModel):
    invitation = models.ForeignKey(Invitation)
    english_name = models.CharField(max_length=200, default="")
    hebrew_name = models.CharField(max_length=200, default="")
    email_internal_use = models.EmailField(default="", blank=True)
    person_RSVP = models.CharField(max_length=200, choices=RSVP_choices, default='Maybe')
    is_vegan = models.BooleanField(default=False)
    diet_info = models.CharField(max_length=200, default="", blank=True)
    needs_ride_location = models.CharField(max_length=200, default="", blank=True)
    has_car_room_location = models.CharField(max_length=200, default="", blank=True)
    number_of_seats = models.IntegerField(default=0)
    email_app = models.EmailField(default="", blank=True)
    phone_app = models.CharField(max_length=15, default="", blank=True)

    def __str__(self):
        return "Invitation: " + str(self.id) + ", name: " + self.english_name





