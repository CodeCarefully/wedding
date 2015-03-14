from django.contrib import admin
from invitation.models import Invitation, Person


class Site(admin.AdminSite):
    pass


site = Site()
site.site_header = "Gavi and Ariela's Admin page!"


#@admin.register(Invitation, Person, site=site)
class PeopleInline(admin.TabularInline):
    model = Person
    extra = 1
    fieldsets = [
        ('Invitation Id', {'fields': ['invitation']}),
        ('Name', {'fields': ['name']}),
        ('Email', {'fields': ['email']}),
        ('RSVP', {'fields': ['person_RSVP']})
    ]


# class InvitationInline(admin.TabularInline):
#     model = Invitation
#


class InvitationAdmin(admin.ModelAdmin):
    inlines = [PeopleInline]
    fieldsets = [
        ('Invitation Name', {'fields': ['invitation_name']}),
        ('Family Invitation?', {'fields': ['family_size', 'family_RSVP', 'family_RSVP_number']}),
        ('With Guest Invitation?', {'fields': ['with_guest', 'guest_RSVP']})
    ]
    list_display = ('invitation_name', 'id')


# class PersonAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Invitation Id', {'fields': ['invitation']}),
#         ('Name', {'fields': ['name']}),
#         ('Email', {'fields': ['email']}),
#         ('RSVP', {'fields': ['person_RSVP']})
#     ]

site.register(Invitation, InvitationAdmin)




