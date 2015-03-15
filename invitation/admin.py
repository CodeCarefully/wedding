from django.contrib import admin
from invitation.models import Invitation, Person


class Site(admin.AdminSite):
    pass


site = Site()
site.site_header = "Gavi and Ariela's Admin page!"


class PeopleInline(admin.StackedInline):
    model = Person
    extra = 1
    fieldsets = [
        ('Info', {'fields': [['english_name', 'hebrew_name', 'email']]}),
        ('Additional Information (to fill if RSVP not through website)',
         {'fields': ['person_RSVP', ['is_vegan', 'diet_info'], 'needs_ride_location', ['has_car_room_location',
                                                                                       'car_room_amount']],
          'classes': ['collapse']})
    ]


# class InvitationInline(admin.TabularInline):
#     model = Invitation
#
# @site.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    inlines = [PeopleInline]
    fieldsets = [
        ('Invitation Name', {'fields': ['invitation_name']}),
        ('With Guest Invitation?', {'fields': ['with_guest']}),
        ('Family Invitation?', {'fields': ['family_size'],
                                'classes': ['wide']}),
        ('Add RSVP (fill if RSVP was not through website)',
         {'classes': ['collapse'],
          'fields': ['guest_RSVP', ['family_RSVP', 'family_RSVP_number']]})
    ]
    list_display = ('invitation_name', 'invite_id', 'was_opened', 'date_opened')
    search_fields = ['invitation_name']
    list_filter = ['was_opened', 'date_opened']


# class PersonAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Invitation Id', {'fields': ['invitation']}),
#         ('Name', {'fields': ['name']}),
#         ('Email', {'fields': ['email']}),
#         ('RSVP', {'fields': ['person_RSVP']})
#     ]

site.register(Invitation, InvitationAdmin)




