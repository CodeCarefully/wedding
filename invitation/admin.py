from django.contrib import admin
from invitation.models import Invitation, Person, str_is_english
from invitation.export import export_all_info, EXPORT_ALL_INFO_NAME
import io
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


def email_guests_initial(InvitationAdmin, request, queryset):
    if "apply" in request.POST:
        emails_sent = 0
        for invite in queryset:
            for person in invite.person_list():
                if person.email:
                    emails_sent += 1
                email_person(person, "initial")
        if emails_sent == 1:
                message_bit = "1 email was"
        else:
            message_bit = "%s emails were" % emails_sent
        InvitationAdmin.message_user(request, "%s successfully sent." % message_bit)
        return HttpResponseRedirect(request.get_full_path())
    else:
        context = {
            'title': "Are you sure?",
            'queryset': queryset,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
        }
        return render_to_response('admin/warn_email.html', context, RequestContext(request))
email_guests_initial.short_description = "Email invitation"



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
    list_display = ('invitation_name', 'invite_id', 'was_opened', 'date_opened', 'invitation_url')
    ordering = ['invitation_name']
    search_fields = ['invitation_name']
    list_filter = ['was_opened', 'date_opened', 'side', 'group']

    actions = [export_all_info_excel, email_guests_initial, statistics_admin_action, set_to_default_action]

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




