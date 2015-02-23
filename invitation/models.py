from django.db import models


class RSVPState():
    yes = 1
    maybe = 2
    no = 0


class Invitation(models.Model):
    with_guest = models.BinaryField()
    family_size = models.IntegerField(default=0)
    guest_RSVP = models.IntegerField(default=RSVPState.maybe)
    family_RSVP = models.IntegerField(default=RSVPState.maybe)
    family_RSVP_number = models.IntegerField(default=0)


class Person(models.Model):
    invitation = models.ForeignKey(Invitation)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    person_RSVP = models.IntegerField(default=RSVPState.maybe)