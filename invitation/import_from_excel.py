__author__ = 'User'

import xlrd
from invitation.models import Invitation, Person, group_choices, side_choices
group_choices = {group[0] for group in group_choices}
side_choices = {side[0] for side in side_choices}

table_map = {
    "en_name": 4,
    "heb_name": 5,
    "group": 1,
    "side": 2,
    "email": 6,
    "invite_name": 3,
    "language": 7
}

invite_by_name = {}


def import_from_excel():
    try:
        wb = xlrd.open_workbook("C:\\Users\\User\\Documents\\GitHub\\wedding\\invitation\\list.xlsx")
    except FileNotFoundError:
        return
    sheet = wb.sheet_by_index(0)
    for row in range(sheet.nrows):
        invite_name = sheet.cell_value(row, table_map["invite_name"])
        if not invite_name:
            continue
        insert_row(invite_name, sheet.row_values(row))


def make_new_invite(row_values):
    invite = Invitation()
    group = row_values[table_map["group"]]
    group = group.replace("Bride", "").strip()
    group = group.replace("Groom", "").strip()
    if group in group_choices:
        invite.group = group
    else:
        invite.group = ["Other"]
    side = row_values[table_map["side"]]
    if side in side_choices:
        invite.side = side
    invite.language = row_values[table_map["language"]]
    invite.invitation_name = row_values[table_map["invite_name"]]
    invite.save()
    return invite


def insert_row(invite_name, row_values):
    invite = get_invitation(invite_name)
    if invite is None:
        invite = make_new_invite(row_values)
    add_person(invite, row_values)


def add_person(invite, row_values):
    for person in invite.person_set.all():
        if (person.hebrew_name == row_values[table_map["heb_name"]] and
                    person.english_name == row_values[table_map["en_name"]]):
            return
    person = Person()
    person.invitation = invite
    person.hebrew_name = row_values[table_map["heb_name"]]
    person.english_name = row_values[table_map["en_name"]]
    person.email = row_values[table_map["email"]]
    person.save()

def get_invitation(requested_invite_name):
    invite = invite_by_name.get(requested_invite_name, None)
    if invite:
        return invite
    invites = Invitation.objects.filter(invitation_name=requested_invite_name)
    if len(invites) > 1:
        raise Exception("bad database!")
    if len(invites) == 1:
        return invites[0]
    return None
