__author__ = 'User'

import xlsxwriter


EXPORT_NAME = "export.xlsx"
titles = {
    (0,): "",
    (1,): "",
    (2, 3): "שיוך",
    (4, 5, 6): "פרטי התקשרות",
    (7, 8, 9, 10): "כתובת",
    (11,): "",
    (12,): ""
}

index = {
    "name": {"col": 0, "title": "הזמנה לכבוד"},
    "# invited": {"col": 1, "title": "מס' אורחים שהוזמנו"},
    "side": {"col": 2, "title": "צד"},
    "group": {"col": 3, "title": "קבוצה"},
    "phone": {"col": 4, "title": "סלולרי"},
    "home phone": {"col": 5, "title": "טלפון רגיל"},
    "email": {"col": 6, "title": "אימייל"},
    "city": {"col": 7, "title": "עיר"},
    "street": {"col": 8, "title": "רחוב"},
    "zip code": {"col": 9, "title": "מיקוד"},
    "POB": {"col": 10, "title": "תא דואר"},
    "check": {"col": 11, "title": "צ'ק צפוי"},
    "# coming": {"col": 12, "title": "אישרו שיגיעו"},
}

mapping = {
    "Both": "חתן,כלה",
    "Bride": "כלה",
    "Groom": "חתן",
    "Friends": "חברים",
    'Family': "משפחה",
    "Work": "עבודה",
    'School': "לימודים",
    'Army': "צבע",
    'Other': "אחר",
    "": "",
    None: "",
    "Yes": 1,
    "No": 0,
    "Maybe": 0
}


def export_to_excel(invitation_list):
    workbook = xlsxwriter.Workbook(EXPORT_NAME)
    title_format = workbook.add_format({'align': 'center', 'bg_color': '#366092', 'border': 1, 'font_color': 'white'})
    reg_format = workbook.add_format({'border': 1})
    work_sheet = workbook.add_worksheet()
    row = write_titles(work_sheet, title_format)
    for invite in invitation_list:
        row = write_invitations(work_sheet, invite, row, reg_format)
    work_sheet.set_column('F:F', 20,  reg_format, {'hidden': 1})
    work_sheet.set_column('H:L', 20,  reg_format, {'hidden': 1})
    workbook.close()


def write_titles(work_sheet, title_format):
    row = 0
    for cols in titles:
        titles_text = titles[cols]
        if len(cols) > 1:
            work_sheet.merge_range(row, cols[0], row, cols[-1], titles_text, title_format)
        else:
            work_sheet.write(row, cols[0], titles_text, title_format)
    row += 1
    for cell_type in index:
        titles_text = index[cell_type]["title"]
        col = index[cell_type]["col"]
        work_sheet.write(row, col, titles_text, title_format)
    row += 1
    return row


def write_invitations(work_sheet, invite, row, reg_format):
    export_list = []
    guest_list = invite.person_list()
    guest_number = 0
    if invite.has_guest_person():
        invite.couple = True
        invite.save()
    while guest_number < len(guest_list):
        export_line = {}
        if invite.couple and guest_number == 0 and len(guest_list) >= 2:
            guest_1 = guest_list[0]
            guest_2 = guest_list[1]
            and_text = " and "
            if not invite.is_english():
                and_text = " ו"
            name = guest_1.name.strip() + and_text + guest_2.name.strip()
            invited = 2
            coming = mapping[guest_1.person_rsvp] + mapping[guest_2.person_rsvp]
            email = guest_1.email_app
            phone = guest_1.phone_app
            guest_number += 2
        else:
            guest = guest_list[guest_number]
            name = guest.name
            invited = 1
            coming = mapping[guest.person_rsvp]
            email = guest.email_app
            phone = guest.phone_app
            guest_number += 1
        export_line["name"] = name
        export_line["# invited"] = invited
        export_line["# coming"] = coming
        export_line["side"] = mapping[invite.side]
        export_line["group"] = mapping[invite.group]
        export_line["phone"] = phone
        export_line["email"] = email
        export_list.append(export_line)
    for line in export_list:
        for attribute in line:
            text = line[attribute]
            col = index[attribute]["col"]
            work_sheet.write(row, col, text, reg_format)
        row += 1
    return row
