from django.db import models
from django.utils import timezone
from random import randint
import string


class BaseModel(models.Model):
    modified_date = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.modified_date = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)


rsvp_choices = [('Yes', 'Yes'), ('Maybe', 'Maybe'), ('No', 'No')]
language_choices = [('English', 'English'), ('Hebrew', 'Hebrew')]
diet_choices = [
    ('Vegetarian', 'Vegetarian'),
    ('Vegan', 'Vegan'),
    ('Glatt', 'Glatt Kosher'),
    ('GlutenFree', 'Gluten Free')
]
side_choices = [('Bride', 'Bride'), ('Groom', 'Groom'), ('Both', 'Both')]
group_choices = [
    ('Friends', 'Friends'),
    ('Family', 'Family'),
    ('GL\'s', 'GL\'s'),
    ('Debate', 'Debate'),
    ('Mother Family', 'Mother Family'),
    ('Father Family', 'Father Family'),
    ('Parent Friends', 'Parent Friends'),
    ('Mother Friends', 'Father Friends'),
    ('Other', 'Other'),
    ("Beit Shemesh", "Beit Shemesh"),
    ("Other Friends", "Other Friends"),
    ("Moskovitz", "Moskovitz"),
    ("Shaham", "Shaham")
]


def str_is_english(_str):
    _str = _str.strip()
    for char in _str:
        if char in string.ascii_letters:
            return True
    return False


def is_id_good(invite_id):
    """Checks if the ID generated is Unique in the DB"""
    all_invitations = Invitation.objects.all()
    for other_invite_id in [invite.invite_id for invite in all_invitations]:
        if other_invite_id == invite_id:
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
    with_guest = models.BooleanField(default=False, verbose_name="Invite a +1 with guest")
    invitation_name = models.CharField(max_length=200, default="", blank=True, verbose_name="Invite name")
    date_opened = models.DateTimeField(default=timezone.datetime(2000, 1, 1))
    was_opened = models.BooleanField(default=False)
    side = models.CharField(max_length=200, choices=side_choices, default='Both')
    group = models.CharField(max_length=200, choices=group_choices, blank=True)
    language = models.CharField(max_length=200, choices=language_choices, default='English')
    # couple = models.BooleanField(default=True)

    def set_invite_to_default(self):
        self.date_opened = timezone.datetime(2000, 1, 1)
        self.was_opened = False
        for person in self.person_list():
            person.person_rsvp = "Maybe"
            person.diet_choices = ''
            person.save()
        self.save()

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
        else:
            return "People"

    def total_yes(self):
        """Total people who are coming"""
        return self.total_rsvp("Yes")

    def total_maybe(self):
        """Total people who are coming"""
        return self.total_rsvp("Maybe")

    def total_no(self):
        """Total people who are coming"""
        return self.total_rsvp("No")

    def total_rsvp(self, rsvp):
        """Total people who are coming"""
        total_rsvp = 0
        people = Person.objects.filter(invitation=self.id)
        for person in people:
            if person.person_rsvp == rsvp:
                total_rsvp += 1
        return total_rsvp

    def invitation_total_invited(self):
        total_invited = 0
        people = Person.objects.filter(invitation=self.id)
        for _ in people:
            total_invited += 1
        return total_invited

    def create_guest(self):
        if not self.has_guest_person():
            guest = Person()
            guest.invitation = self
            guest.english_name = "Guest"
            guest.hebrew_name = "אורח/ת"
            guest.save()
            self.save()

    def is_english(self):
        if self.language == 'English':
            return True

    def __str__(self):
        return str(self.id)

    def has_guest_person(self):
        people = Person.objects.filter(invitation=self.id)
        for person in people:
            if person.is_guest():
                return True
        return False

    def person_list(self):
        person_list = list(self.person_set.all())
        for person in person_list[:]:
            if person.is_guest():
                person_list.remove(person)
                person_list.append(person)
        return person_list

    def has_rsvped(self):
        for person in self.person_list():
            if person.has_rsvp():
                return True
        return False

    def has(self, rsvp):
        for person in self.person_list():
            if person.person_rsvp == rsvp:
                return True
        return False

    def invitation_url(self):
        return "http://streytanwedding.com/invitation/" + self.invite_id

    def person_coming_list(self):
        coming_list = []
        for person in self.person_list():
            if person.is_coming():
                coming_list.append(person)
        return coming_list

    def needs_rsvp(self):
        invite_needs_rsvp = False
        for person in self.person_list():
            if not person.has_rsvp():
                invite_needs_rsvp = True
        return invite_needs_rsvp


class Person(BaseModel):
    invitation = models.ForeignKey(Invitation)
    english_name = models.CharField(max_length=200, default="")
    hebrew_name = models.CharField(max_length=200, default="")
    email = models.EmailField(default="", blank=True)
    person_rsvp = models.CharField(max_length=200, choices=rsvp_choices, default='Maybe')
    diet_choices = models.CharField(max_length=200, choices=diet_choices, blank=True, verbose_name="Diet info")

    def __str__(self):
        return self.english_name

    def is_guest(self):
        if self.english_name in {"Guest", "אורח/ת", "אורח\ת"}:
            return True
        else:
            return False

    def name(self):
        invite = self.invitation
        if invite.is_english():
            return self.english_name
        else:
            return self.hebrew_name

    def is_coming(self):
        return self.person_rsvp == "Yes"

    def has_rsvp(self):
        return self.person_rsvp in {"Yes", "No"}