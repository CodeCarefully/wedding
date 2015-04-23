__author__ = 'User'

import xlsxwriter

EXPORT_ALL_INFO_NAME = "C:\\Users\\User\\Documents\\GitHub\\wedding\\all_info.xlsx"

all_info_index = [
    "invitation #",
    "invitation name",
    "guest english name",
    "guest hebrew name",
    "RSVP",
    "# invited",
    "# coming",
    "date opened",
    "diet info",
    "side",
    "group",
    "email",
    "url"
]


def make_couple_name(guest_1, guest_2, and_text):
    names_1 = guest_1.english_name.split(" ")
    names_2 = guest_2.english_name.split(" ")
    if names_1[-1] == names_2[-1]:
        names_1 = names_1[:-1]
    names_1, names_2 = " ".join(names_1), " ".join(names_2)
    return names_1.strip() + and_text + names_2.strip()


def write_invite(sheet, invite, reg_format, index):
    invite_num = invite.invite_id
    is_family = invite.is_family
    invite_name = invite.invitation_name
    side = invite.side
    group = invite.group
    invited = invite.invitation_total_invited() if is_family else 1
    coming = invite.invitation_total_rsvp() if is_family else 0
    date_opened = str(invite.date_opened)[:16] if invite.date_opened.year == 2015 else " "
    url = invite.invitation_url()
    for i, guest in enumerate(invite.person_list()):
        guest_english_name = guest.english_name
        guest_hebrew_name = guest.hebrew_name
        rsvp = guest.person_rsvp
        if guest.is_coming():
            coming = 1
        diet_info = guest.diet_blank if guest.diet_choices == "Other" else guest.diet_choices
        email = guest.email
        # Start printing
        write_row_col(sheet, "invitation #", invite_num, reg_format, index)
        write_row_col(sheet, "invitation name", invite_name, reg_format, index)
        write_row_col(sheet, "guest english name", guest_english_name, reg_format, index)
        write_row_col(sheet, "guest hebrew name", guest_hebrew_name, reg_format, index)
        write_row_col(sheet, "RSVP", rsvp, reg_format, index)
        write_row_col(sheet, "# invited", invited, reg_format, index)
        write_row_col(sheet, "# coming", coming, reg_format, index)
        write_row_col(sheet, "date opened", date_opened, reg_format, index)
        write_row_col(sheet, "diet info", diet_info, reg_format, index)
        write_row_col(sheet, "side", side, reg_format, index)
        write_row_col(sheet, "group", group, reg_format, index)
        write_row_col(sheet, "email", email, reg_format, index)
        write_row_col(sheet, "url", url, reg_format, index)
        sheet["row"] += 1


def write_row_col(sheet, info_type, to_insert, reg_format, index):
    if info_type in index:
        col = index.index(info_type)
        sheet["sheet"].write(sheet["row"], col, to_insert, reg_format)


def export_all_info(invitation_list, index=all_info_index):
    workbook = xlsxwriter.Workbook(EXPORT_ALL_INFO_NAME)
    reg_format = workbook.add_format({'border': 1})
    title_format = workbook.add_format({'align': 'center', 'bg_color': '#D682FC', 'border': 1})
    sheet = {"sheet": workbook.add_worksheet(), "row": 0}
    for col, title in enumerate(index):
        sheet["sheet"].write(sheet["row"], col, title, title_format)
    sheet["row"] += 1
    for invite in invitation_list:
        write_invite(sheet, invite, reg_format, index)
    for col in range(17):
        if col in {4, 5, 6}:
            sheet["sheet"].set_column(col, col, 8)
        else:
            sheet["sheet"].set_column(col, col, 15)
    workbook.close()