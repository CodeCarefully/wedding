from django.db import models
from django.utils import timezone
from random import randint


class BaseModel(models.Model):
    modified_date = models.DateTimeField(auto_now=True, default=timezone.now())

    class Meta:
        abstract = True


rsvp_choices = [('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')]
side_choices = [('Bride', 'Bride'), ('Groom', 'Groom'), ('Both', 'Both')]
group_choices = [
    ('Bride Friends', 'Bride Friends'),
    ('Bride Family', 'Bride Family'),
    ('Groom Friends', 'Groom Friends'),
    ('Groom Family', 'Groom Family'),
]


def is_id_good(invite_id):
    """Checks if the ID generated is Unique in the DB"""
    all_invitations = Invitation.objects.all()
    for id in [invite.invite_id for invite in all_invitations]:
        if id == invite_id:
            return False
    return True


def id_generator():
    """Generated random ID to be used as invite codes"""
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
    family_rsvp = models.CharField(max_length=200, choices=rsvp_choices, default='Maybe')
    family_rsvp_number = models.IntegerField(default=0)
    personal_message = models.TextField(max_length=400, default="", blank=True)
    invitation_name = models.CharField(max_length=200, default="", blank=True)
    date_opened = models.DateTimeField(default=timezone.datetime(2000, 1, 1))
    was_opened = models.BooleanField(default=False)
    side = models.CharField(max_length=200, choices=side_choices, default='Both')
    group = models.CharField(max_length=200, choices=group_choices, blank=True)

    def invitation_type(self):
        """
        Returns the invitation type.
        -- Guest means that there is an extra person to the invitation who is a guest.
        -- Family means that we are just inputting the family name and size and the invite
        has one person just for the info.
        -- People type means the invitation includes a list of people
        """
        if self.with_guest:
            return "Guest"
        elif self.family_size > 0:
            return "Family"
        else:
            return "People"

    def invitation_total_rsvp(self):
        """Total people who are coming"""
        total_rsvp = 0
        if self.family_size and self.family_rsvp == "Yes":
            return self.family_rsvp_number
        people = Person.objects.filter(invitation=self.id)
        for person in people:
            if person.person_rsvp == "Yes":
                total_rsvp += 1
        return total_rsvp

    def invitation_total_invited(self):
        total_invited = 0
        if self.family_size:
            return self.family_size
        people = Person.objects.filter(invitation=self.id)
        for _ in people:
            total_invited += 1
        return total_invited

    def create_guest(self):
        guest = Person()
        guest.invitation = self
        guest.english_name = "Guest"
        guest.hebrew_name = "אורח"
        guest.save()
        self.save()

    def __str__(self):
        return str(self.id)

    def has_guest_person(self):
        people = Person.objects.filter(invitation=self.id)
        for person in people:
            if person.english_name == 'Guest':
                return True
        return False


class Person(BaseModel):
    invitation = models.ForeignKey(Invitation)
    english_name = models.CharField(max_length=200, default="")
    hebrew_name = models.CharField(max_length=200, default="")
    email_internal_use = models.EmailField(default="", blank=True)
    person_rsvp = models.CharField(max_length=200, choices=rsvp_choices, default='Maybe')
    is_vegan = models.BooleanField(default=False)
    diet_info = models.CharField(max_length=200, default="", blank=True)
    needs_ride_location = models.CharField(max_length=200, default="", blank=True)
    has_car_room_location = models.CharField(max_length=200, default="", blank=True)
    number_of_seats = models.IntegerField(default=0)
    email_app = models.EmailField(default="", blank=True)
    phone_app = models.CharField(max_length=15, default="", blank=True)

    def __str__(self):
        return "Invitation: " + str(self.id) + ", name: " + self.english_name





