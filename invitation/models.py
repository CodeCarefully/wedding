from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    # created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True, default=timezone.now())

    class Meta:
        abstract = True


class RSVPState():
    yes = "Yes"
    maybe = "Maybe"
    no = "No"


class Invitation(BaseModel):
    # TODO invitation_utl_id = models.IntegerField(default=0)
    with_guest = models.BooleanField(default=False)
    family_size = models.IntegerField(default=0)
    guest_RSVP = models.CharField(max_length=200, default=RSVPState.maybe)
    family_RSVP = models.CharField(max_length=200, default=RSVPState.maybe)
    family_RSVP_number = models.IntegerField(default=0)
    invitation_total_RSVP = models.IntegerField(default=0)
    personal_message = models.CharField(max_length=400, default=" ")
    invitation_name = models.CharField(max_length=200, default="")

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
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default=" ")
    person_RSVP = models.CharField(max_length=200, default=RSVPState.maybe)
    is_vegan = models.BooleanField(default=False)
    diet_info = models.CharField(max_length=200, default=" ")
    needs_ride_location = models.CharField(max_length=200, default=" ")
    has_car_room_location = models.CharField(max_length=200, default=" ")
    car_room_amount = models.IntegerField(default=0)

    def __str__(self):
        return "Invitation: " + str(self.id) + ", name: " + self.name



