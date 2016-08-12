from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from invitation.models import Invitation, Person, diet_choices
from django.utils import timezone
from invitation.export import export_all_info, EXPORT_ALL_INFO_NAME
from invitation.import_from_excel import import_from_excel


def get_pk_from_id(invite_id):
    for invite in Invitation.objects.all():
        if invite.invite_id == invite_id:
            return invite.pk
    return 0


@ensure_csrf_cookie
def invitation_detail(request, invite_id, lang=None):
    pk = get_pk_from_id(invite_id)
    try:
        invitation = Invitation.objects.get(pk=pk)
    except:
        return render(request, 'invitation/404.html')
    invitation.was_opened = True
    invitation.date_opened = timezone.now()
    invitation.save()
    if not lang:
        if invitation.language == "English":
            return HttpResponseRedirect("en")
        else:
            return HttpResponseRedirect("he")
    return render(request, 'invitation/with_code.html', {'invitation': invitation, 'language': lang})


def main_without_code(request, lang=None):
    if not lang:
        return HttpResponseRedirect("/he")
    return render(request, 'invitation/without_code.html', {'language': lang})


def invitation_input_rsvp(request, invite_id, guest_id, rsvp):
    guest_pk = guest_id
    guest = get_object_or_404(Person, pk=guest_pk)
    guest.person_rsvp = rsvp
    guest.save()
    return HttpResponse('')


def invitation_input_diet(request, invite_id, guest_id, diet):
    guest_pk = guest_id
    guest = get_object_or_404(Person, pk=guest_pk)
    if diet in [x[0] for x in diet_choices]:
        guest.diet_choices = diet
        guest.save()
    if diet == "None":
        guest.diet_choices = ''
        guest.save()
    return HttpResponse('')


def input_post_data(request, guest_id):
    post_info = request.POST
    guest_pk = guest_id
    guest = get_object_or_404(Person, pk=guest_pk)
    if "dietaryInfo" in post_info:
        guest.diet_blank = post_info["dietaryInfo"]
        guest.save()
    return HttpResponse('')


def export_all(request):
    all_invitations = Invitation.objects.all()
    export_all_info(all_invitations)
    output = open(EXPORT_ALL_INFO_NAME, "rb")
    output.seek(0)
    response = HttpResponse(output.read(),
                            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = "attachment; filename=All_info.xlsx"
    return response

def import_from_excel_view(request):
    import_from_excel()
    return HttpResponse('')