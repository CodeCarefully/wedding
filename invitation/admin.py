from django.contrib import admin
from invitation.models import Invitation, Person


class PeopleInline(admin.TabularInline):
    model = Person
    extra = 1


class InvitationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Change if Invitation is for a family', {'fields': ['family_size']}),
        ('Check if Invitation includes a guest', {'fields': ['with_guest']})
    ]

    list_display = ('id',)
    inlines = [PeopleInline]

admin.site.register(Invitation, InvitationAdmin)