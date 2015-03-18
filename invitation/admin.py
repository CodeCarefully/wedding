from django.contrib import admin
from invitation.models import Invitation, Person
from django.http import HttpResponseRedirect


def export_selected_objects(invitationadmin, request, queryset):
    selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)

    return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))
export_selected_objects.short_description = 'Export data for these objects'


class Site(admin.AdminSite):
    pass


site = Site()
site.site_header = "Gavi and Ariela's Admin page!"


class PeopleInline(admin.StackedInline):
    model = Person
    extra = 1
    fieldsets = [
        ('Info', {'fields': [['english_name', 'hebrew_name', 'email_internal_use']]}),
        ('Additional Information (to fill if RSVP not through website)',
            {'fields': ['person_RSVP', ['is_vegan', 'diet_info'],
                        'needs_ride_location', ['has_car_room_location', 'number_of_seats']],
             'classes': ['collapse']}),
        ('Info for application.  Input only with user approval!',
         {'fields': [['email_app', 'phone_app']],
          'classes': ['collapse']})
    ]


# class InvitationInline(admin.TabularInline):
#     model = Invitation
#
# @site.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    inlines = [PeopleInline]
    fieldsets = [
        ('Invitation Info', {'fields': [['invitation_name', 'side', 'group']]}),
        ('With Guest Invitation?', {'fields': ['with_guest']}),
        ('Family Invitation?', {'fields': ['family_size'],
                                'classes': ['wide']}),
        ('Add RSVP (fill if RSVP was not through website)',
         {'classes': ['collapse'],
          'fields': ['guest_RSVP', ['family_RSVP', 'family_RSVP_number']]})
    ]
    list_display = ('invitation_name', 'invite_id', 'was_opened', 'date_opened')
    search_fields = ['invitation_name']
    list_filter = ['was_opened', 'date_opened', 'side', 'group']
    actions = ['export_selected_objects']


# class PersonAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Invitation Id', {'fields': ['invitation']}),
#         ('Name', {'fields': ['name']}),
#         ('Email', {'fields': ['email']}),
#         ('RSVP', {'fields': ['person_RSVP']})
#     ]

site.add_action(export_selected_objects)
site.register(Invitation, InvitationAdmin)




