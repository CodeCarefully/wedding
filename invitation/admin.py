from django.contrib import admin, messages
from invitation.models import Invitation, Person
from invitation.export import export_all_info, EXPORT_ALL_INFO_NAME
from invitation.export import make_couple_name
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from adminplus.sites import AdminSitePlus
from invitation.statistics import Statistics
from invitation.email import email_person
from django.contrib.admin import helpers

site = AdminSitePlus()
site.site_header = "Devora and Avichai's Admin page!"

email_templates = ["initial"]


def set_to_default_action(InvitationAdmin, request, queryset):
    for invite in queryset:
        invite.set_invite_to_default()
    InvitationAdmin.message_user(request, "{} invites set back to default.".format(len(queryset)))
set_to_default_action.short_description = "Change invitations back to default"


def export_all_info_excel(InvitationAdmin, request, queryset):
    export_all_info(queryset)
    output = open(EXPORT_ALL_INFO_NAME, "rb")
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=All_info.xlsx"
    return response

export_all_info_excel.short_description = "Export all info to excel"


def email_invitation_type(InvitationAdmin, invitations_list, request, email_type):
        emails_sent = 0
        for invite in invitations_list:
            person_list = invite.person_list()
            for i, person in enumerate(person_list):
                if i < 2 and len(person_list) > 1 and not invite.has_guest_person():
                    and_text = " and " if invite.is_english() else " ו"
                    name = make_couple_name(person_list[0], person_list[1], and_text, only_english=False)
                else:
                    name = person.name()
                emails_sent += email_person(person, name, email_type)
        if emails_sent == 1:
            InvitationAdmin.message_user(request, "1 email wes successfully sent")
        elif emails_sent == 0:
            InvitationAdmin.message_user(request, "No emails were sent", level=messages.ERROR)
        else:
            InvitationAdmin.message_user(request, "{} emails were successfully sent".format(emails_sent))


def email_guests_initial(InvitationAdmin, request, queryset):
    if "apply" in request.POST:
        invitations_list = [invite for invite in queryset if invite.needs_rsvp() and not invite.was_opened]
        email_invitation_type(InvitationAdmin, invitations_list, request, "initial")
        return HttpResponseRedirect(request.get_full_path())
    else:
        context = {
            'title': "Are you sure?",
            'queryset': queryset,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        }
        return render_to_response('admin/warn_email.html', context, RequestContext(request))
email_guests_initial.short_description = "Email initial invitation"


def email_guests_opened_reminder(InvitationAdmin, request, queryset):
    if "apply" in request.POST:
        invitations_list = [invite for invite in queryset if invite.needs_rsvp() and invite.was_opened]
        email_invitation_type(InvitationAdmin, invitations_list, request, "opened_reminder")
        return HttpResponseRedirect(request.get_full_path())
    else:
        context = {
            'title': "Are you sure?",
            'queryset': queryset,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        }
        return render_to_response('admin/warn_reminder_email.html', context, RequestContext(request))
email_guests_opened_reminder.short_description = "Email reminder"


def statistics_admin_action(InvitationAdmin, request, queryset):
    stats = Statistics(queryset)
    return render(request, 'admin/statistics.html', {'stats': stats})
statistics_admin_action.short_description = "Get statistics for these invitation only"


class PeopleInline(admin.StackedInline):
    model = Person
    extra = 1
    verbose_name = "Guest"
    verbose_name_plural = "Guests in the invitation"
    fieldsets = [
        ('Input guest',
            {'fields': (('english_name', 'hebrew_name', 'email'), )}),
        ('Additional Information (fill if the rsvp was not through the website)',
            {'fields': ('person_rsvp', ('diet_choices', 'diet_blank')),
             'classes': ('collapse', )})
    ]


class InvitationAdmin(admin.ModelAdmin):
    model = Invitation
    inlines = [PeopleInline]
    fieldsets = [
        ('Invitation Info',
            {'fields': (('invitation_name', 'side', 'group', 'language'), ('with_guest', ))}),
        ('Fill for large family Invitation',
            {'fields': (('is_family', 'family_size'), )}),
        ('Add family rsvp (fill if the rsvp was not through the website)',
            {'classes': ('collapse', ),
             'fields': (('family_rsvp_number',), )})
    ]
    list_per_page = 30
    list_display = ('invitation_name', 'invite_id', 'has_rsvped', 'invitation_total_rsvp', 'date_opened', 'invitation_url')
    ordering = ['invitation_name']
    search_fields = ['invitation_name']
    list_filter = ['was_opened', 'date_opened', 'side', 'group']

    actions = [export_all_info_excel, email_guests_initial, email_guests_opened_reminder, statistics_admin_action, set_to_default_action]

    def save_model(self, request, obj, form, change):
        """Add and remove guest person using the checkbox"""
        obj.save()
        has_guest = obj.has_guest_person()
        if not has_guest and obj.with_guest:
            obj.create_guest()
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




