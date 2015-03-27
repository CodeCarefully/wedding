from django.contrib import admin
from invitation.models import Invitation, Person, str_is_english
from django.http import HttpResponseRedirect


class Site(admin.AdminSite):
    pass


site = Site()
site.site_header = "Gavi and Ariela's Admin page!"


class PeopleInline(admin.StackedInline):
    model = Person
    extra = 1
    verbose_name = "Guest"
    verbose_name_plural = "Guests in the invitation"
    fieldsets = [
        ('Info (add name in the language you want it to be in the invitation)',
            {'fields': [['name', 'email_internal_use']]}),
        ('Additional Information (fill if the rsvp was not through the website)',
            {'fields': ['person_rsvp', ['is_vegan', 'diet_info'],
                        'needs_ride_location', ['has_car_room_location', 'number_of_seats']],
             'classes': ['collapse']}),
        ('Info for application.  Input only with user approval!',
         {'fields': [['email_app', 'phone_app']],
          'classes': ['collapse']})
    ]


class InvitationAdmin(admin.ModelAdmin):
    model = Invitation
    inlines = [PeopleInline]
    fieldsets = [
        ('Invitation Info   (couple means the first two people are a couple)',
            {'fields': [['invitation_name', 'side', 'group'], ['couple', 'with_guest']]}),
        ('Family Invitation?  (as unit, not list of names)',
            {'fields': ['family_size'],
             'classes': ['wide']}),
        ('Add rsvp (fill if the rsvp was not through the website)',
            {'classes': ['collapse'],
             'fields': [['family_rsvp', 'family_rsvp_number']]})
    ]
    list_display = ('invitation_name', 'invite_id', 'was_opened', 'date_opened')
    search_fields = ['invitation_name']
    list_filter = ['was_opened', 'date_opened', 'side', 'group']
    actions = ['export_selected_objects']

    def save_model(self, request, obj, form, change):
        """Add and remove guest person using the checkbox"""
        obj.save()
        has_guest = obj.has_guest_person()
        person_name = request.POST["person_set-0-name"]
        is_english = str_is_english(person_name)
        if not has_guest and obj.with_guest:
            obj.create_guest(is_english)
        if has_guest and not obj.with_guest:
            people = Person.objects.filter(invitation=obj.id)
            for person in people:
                if person.is_guest():
                    person.delete()
        obj.save()


site.register(Invitation, InvitationAdmin)




