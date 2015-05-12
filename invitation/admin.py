from django.contrib import admin, messages
from invitation.models import Invitation, Person, str_is_english
from invitation.export import export_to_hall_excel, EXPORT_HALL_NAME
from invitation.export import export_all_info, EXPORT_ALL_INFO_NAME
from invitation.export import export_rides, EXPORT_RIDES_NAME
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from adminplus.sites import AdminSitePlus
from invitation.statistics import Statistics
from invitation.email import email_invite
from django.contrib.admin import helpers
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _


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


def export_rides_action(InvitationAdmin, request, queryset):
    export_rides(queryset)
    output = open(EXPORT_RIDES_NAME, "rb")
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=Rides_info.xlsx"
    return response

export_rides_action.short_description = "Export rides"


def export_all_info_excel(InvitationAdmin, request, queryset):
    export_all_info(queryset)
    output = open(EXPORT_ALL_INFO_NAME, "rb")
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=All_info.xlsx"
    return response

export_all_info_excel.short_description = "Export all info to excel"


def statistics_admin_action(InvitationAdmin, request, queryset):
    stats = Statistics(queryset)
    return render(request, 'admin/statistics.html', {'stats': stats})
statistics_admin_action.short_description = "Get statistics for these invitation only"


def set_to_default_action(InvitationAdmin, request, queryset):
    for invite in queryset:
        invite.set_invite_to_default()
    InvitationAdmin.message_user(request, "{} invites set back to default.".format(len(queryset)))
set_to_default_action.short_description = "Change invitations back to default"


def email_guests_initial(InvitationAdmin, request, queryset):
    if "apply" in request.POST:
        emails_sent = 0
        invitations_list = [invite for invite in queryset if invite.needs_rsvp() and not invite.was_opened]
        for invite in invitations_list:
            emails_sent += email_invite(invite, "initial")
        if emails_sent == 1:
            InvitationAdmin.message_user(request, "1 email wes successfully sent")
        elif emails_sent == 0:
            InvitationAdmin.message_user(request, "No emails were sent", level=messages.ERROR)
        else:
            InvitationAdmin.message_user(request, "{} emails were successfully sent".format(emails_sent))
        return HttpResponseRedirect(request.get_full_path())
    else:
        context = {
            'title': "Are you sure you want to email invitations?",
            'queryset': queryset,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        }
        return render_to_response('admin/warn_email.html', context, RequestContext(request))
email_guests_initial.short_description = "Email initial invitation"


def email_guests_reminder(InvitationAdmin, request, queryset):
    if "apply" in request.POST:
        emails_sent = 0
        invitations_list = [invite for invite in queryset if invite.needs_rsvp() and invite.was_opened]
        for invite in invitations_list:
            emails_sent += email_invite(invite, "opened_reminder")
        if emails_sent == 1:
            InvitationAdmin.message_user(request, "1 email wes successfully sent")
        elif emails_sent == 0:
            InvitationAdmin.message_user(request, "No emails were sent", level=messages.ERROR)
        else:
            InvitationAdmin.message_user(request, "{} emails were successfully sent".format(emails_sent))
        return HttpResponseRedirect(request.get_full_path())
    else:
        context = {
            'title': "Are you sure you want to email invitations?",
            'queryset': queryset,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        }
        return render_to_response('admin/warn_reminder_email.html', context, RequestContext(request))
email_guests_reminder.short_description = "Email reminder invitation"


class PeopleInline(admin.StackedInline):
    model = Person
    extra = 1
    verbose_name = "Guest"
    verbose_name_plural = "Guests in the invitation"
    fieldsets = [
        ('Info (add name in the language you want it to be in the invitation)',
            {'fields': [['name', 'email_internal_use']]}),
        ('Additional Information (fill if the rsvp was not through the website)',
            {'fields': [['person_rsvp', 'diet_info'],
                        'needs_ride_location', ['has_car_room_location', 'number_of_seats']],
             'classes': ['collapse']}),
        ('Info for application.  Input only with user approval!',
         {'fields': [['email_app', 'phone_app']],
          'classes': ['collapse']})
    ]


class HasRsvpedListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("Has RSVPed")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'HasRSVP'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('True', _('Has RSVPed')),
            ('False', _('Has NOT RSVPed')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        all_invitations = Invitation.objects.all()
        if self.value() == 'True':
            pk_list = [invite.pk for invite in all_invitations if not invite.needs_rsvp()]
            return Invitation.objects.filter(pk__in=pk_list)
        if self.value() == 'False':
            pk_list = [invite.pk for invite in all_invitations if invite.needs_rsvp()]
            return Invitation.objects.filter(pk__in=pk_list)


class InvitationAdmin(admin.ModelAdmin):
    model = Invitation
    inlines = [PeopleInline]
    list_per_page = 30
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
    list_display = ('invitation_name', 'invite_id', 'was_opened', 'date_opened',
                    'has_rsvped', 'invitation_total_rsvp', 'invitation_url')
    ordering = ['invitation_name']
    search_fields = ['invitation_name']
    list_filter = ['was_opened', 'date_opened', 'side', 'group', HasRsvpedListFilter]

    actions = [export_to_app_excel, export_all_info_excel, email_guests_initial, email_guests_reminder,
               statistics_admin_action, export_rides_action, set_to_default_action]

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



