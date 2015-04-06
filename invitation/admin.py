from django.contrib import admin
from invitation.models import Invitation, Person, str_is_english
from invitation.export import export_to_hall_excel, EXPORT_HALL_NAME, export_all_info, EXPORT_ALL_INFO_NAME
import io
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from adminplus.sites import AdminSitePlus
from invitation.statistics import Statistics
from invitation.email import email_person

site = AdminSitePlus()
site.site_header = "Gavi and Ariela's Admin page!"

email_templates = ["initial"]


def export_to_app_excel(InvitationAdmin, request, queryset):
    export_to_hall_excel(queryset)
    output = open(EXPORT_HALL_NAME, "rb")
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=Info_for_hall_app.xlsx"
    return response

export_to_app_excel.short_description = "Export to excel for hall"


def export_all_info_excel(InvitationAdmin, request, queryset):
    export_all_info(queryset)
    output = open(EXPORT_ALL_INFO_NAME, "rb")
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=All_info.xlsx"
    return response

export_all_info_excel.short_description = "Export all info to excel"


def email_guests_initial(InvitationAdmin, request, queryset):
    emails_sent = 0
    for invite in queryset:
        for person in invite.person_list():
            if person.email_internal_use:
                emails_sent += 1
            email_person(person, "initial")
    if emails_sent == 1:
            message_bit = "1 email was"
    else:
        message_bit = "%s emails were" % emails_sent
    InvitationAdmin.message_user(request, "%s successfully published." % message_bit)
email_guests_initial.short_description = "Email initial invitation"


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

        # Add for family invitations
        # ('Family Invitation?  (as unit, not list of names)',
        #     {'fields': ['family_size'],
        #      'classes': ['wide']}),
        # ('Add rsvp (fill if the rsvp was not through the website)',
        #     {'classes': ['collapse'],
        #      'fields': [['family_rsvp', 'family_rsvp_number']]})
    ]
    list_display = ('invitation_name', 'invite_id', 'was_opened', 'date_opened', 'invitation_url')
    ordering = ['invitation_name']
    search_fields = ['invitation_name']
    list_filter = ['was_opened', 'date_opened', 'side', 'group']

    actions = [export_to_app_excel, export_all_info_excel, email_guests_initial]

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


def statistics(request):
    stats = Statistics()
    return render(request, 'admin/statistics.html', {'stats': stats})
site.register_view('statistics.html', view=statistics)

site.register(Invitation, InvitationAdmin)




