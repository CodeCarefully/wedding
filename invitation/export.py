__author__ = 'User'

import xlsxwriter


EXPORT_HALL_NAME = "hall_export.xlsx"
EXPORT_ALL_INFO_NAME = "all_info.xlsx"
EXPORT_RIDES_NAME = "ride_info.xlsx"
titles = {
    (0,): "",
    (1,): "",
    (2, 3): "שיוך",
    (4, 5, 6): "פרטי התקשרות",
    (7, 8, 9, 10): "כתובת",
    (11,): "",
    (12,): ""
}

hall_index = {
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
    'Army': "צבא",
    'Other': "אחר",
    'Siblings\' friends': "חברי האחים",
    'Parents\' friends': "חברי ההורים",
    'Family friends': "חברי משפחה",
    'Grandparents\' friends': "חברי הסבים",
    "": "",
    None: "",
    "Yes": 1,
    "No": 0,
    "Maybe": 0
}

all_info_index = [
    "invitation #",
    "invitation name",
    "guest name",
    "plus one",
    "RSVP",
    "side",
    "group",
    "couple",
    "date opened",
    "diet info",
    "needs a ride from",
    "can give a ride from",
    "number of free seats",
    "email",
    "phone number",
    "message"
]

ride_index = {
    "need_ride_invite": {"col": 0, "title": "Invite name"},
    "need_ride_name": {"col": 1, "title": "Guest name"},
    "need_ride_location": {"col": 2, "title": "Location"},
    "has_ride_invite": {"col": 4, "title": "Invite name"},
    "has_ride_name": {"col": 5, "title": "Guest name"},
    "has_ride_location": {"col": 6, "title": "Location"},
    "has_ride_seats": {"col": 7, "title": "Free seats"}
}


def write_ride_titles(sheet, title_format):
    sheet["sheet"].merge_range(0, ride_index["need_ride_invite"]["col"], 0,
                               ride_index["need_ride_location"]["col"], "Need a ride", title_format)
    sheet["sheet"].merge_range(0, ride_index["has_ride_invite"]["col"], 0,
                               ride_index["has_ride_seats"]["col"], "Can provide a ride", title_format)
    for key in ride_index:
        sheet["sheet"].write(1, ride_index[key]["col"], ride_index[key]["title"], title_format)


def add_need_ride(sheet, person, reg_format):
    row = sheet["need_ride_row"]
    sheet["sheet"].write(row, ride_index["need_ride_name"]["col"], person.name, reg_format)
    sheet["sheet"].write(row, ride_index["need_ride_location"]["col"], person.needs_ride_location, reg_format)
    invite_name = person.invitation.invitation_name
    sheet["sheet"].write(row, ride_index["need_ride_invite"]["col"], invite_name, reg_format)
    sheet["need_ride_row"] += 1


def add_has_ride(sheet, person, reg_format):
    row = sheet["has_ride_row"]
    sheet["sheet"].write(row, ride_index["has_ride_name"]["col"], person.name, reg_format)
    sheet["sheet"].write(row, ride_index["has_ride_location"]["col"], person.has_car_room_location, reg_format)
    sheet["sheet"].write(row, ride_index["has_ride_seats"]["col"], person.number_of_seats, reg_format)
    invite_name = person.invitation.invitation_name
    sheet["sheet"].write(row, ride_index["has_ride_invite"]["col"], invite_name, reg_format)
    sheet["has_ride_row"] += 1


def export_rides(invitation_list):
    workbook = xlsxwriter.Workbook(EXPORT_RIDES_NAME)
    reg_format = workbook.add_format({'border': 1})
    title_format = workbook.add_format({'align': 'center', 'bg_color': '#D682FC', 'border': 1})
    sheet = {"sheet": workbook.add_worksheet(), "has_ride_row": 2, "need_ride_row": 2}
    write_ride_titles(sheet, title_format)
    for invite in invitation_list:
        for person in invite.person_list():
            if person.has_car_room_location and person.is_coming():
                add_has_ride(sheet, person, reg_format)
            if person.needs_ride_location and person.is_coming():
                add_need_ride(sheet, person, reg_format)
    for col in range(17):
        if col == 3:
            sheet["sheet"].set_column(col, col, 5)
        else:
            sheet["sheet"].set_column(col, col, 15)
    workbook.close()


def export_to_hall_excel(invitation_list):
    workbook = xlsxwriter.Workbook(EXPORT_HALL_NAME)
    title_format = workbook.add_format({'align': 'center', 'bg_color': '#366092', 'border': 1, 'font_color': 'white'})
    reg_format = workbook.add_format({'border': 1})
    sheet = {"sheet": workbook.add_worksheet(), "row": 0}
    write_titles(sheet, title_format)
    for invite in invitation_list:
        write_invitations(sheet, invite, reg_format)
    for col in range(50):
        sheet["sheet"].set_column(col, col, 15)
    sheet["sheet"].set_column('F:F', 20,  reg_format, {'hidden': 1})
    sheet["sheet"].set_column('H:L', 20,  reg_format, {'hidden': 1})

    workbook.close()


def write_titles(work_sheet, title_format):
    row = work_sheet["row"]
    for cols in titles:
        titles_text = titles[cols]
        if len(cols) > 1:
            work_sheet["sheet"].merge_range(row, cols[0], row, cols[-1], titles_text, title_format)
        else:
            work_sheet["sheet"].write(row, cols[0], titles_text, title_format)
    work_sheet["row"] += 1
    for cell_type in hall_index:
        titles_text = hall_index[cell_type]["title"]
        col = hall_index[cell_type]["col"]
        work_sheet["sheet"].write(work_sheet["row"], col, titles_text, title_format)
    work_sheet["row"] += 1


def make_couple_name(guest_1, guest_2, and_text):
    names_1 = guest_1.name.split(" ")
    names_2 = guest_2.name.split(" ")
    if names_1[-1] == names_2[-1]:
        names_1 = names_1[:-1]
    names_1, names_2 = " ".join(names_1), " ".join(names_2)
    return names_1.strip() + and_text + names_2.strip()


def write_invitations(work_sheet, invite, reg_format):
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
            name = make_couple_name(guest_1, guest_2, and_text)
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
            col = hall_index[attribute]["col"]
            work_sheet["sheet"].write(work_sheet["row"], col, text, reg_format)
        work_sheet["row"] += 1


def write_invite(sheet, invite, reg_format, index):
    invite_num = invite.invite_id
    invite_name = invite.invitation_name
    with_guest = "Yes" if invite.with_guest else " "
    side = invite.side
    group = invite.group
    date_opened = str(invite.date_opened)[:16] if invite.date_opened.year == 2015 else " "
    message = invite.personal_message
    for i, guest in enumerate(invite.person_list()):
        couple = "Yes" if i < 2 and (invite.with_guest or invite.couple) else " "
        guest_name = guest.name
        rsvp = guest.person_rsvp
        diet_info = guest.diet_info
        needs_ride_loc = guest.needs_ride_location
        has_ride_loc = guest.has_car_room_location
        car_room = guest.number_of_seats
        email = guest.email_internal_use
        phone = guest.phone_app
        # Start printing
        write_row_col(sheet, "invitation #", invite_num, reg_format, index)
        write_row_col(sheet, "invitation name", invite_name, reg_format, index)
        write_row_col(sheet, "guest name", guest_name, reg_format, index)
        write_row_col(sheet, "plus one", with_guest, reg_format, index)
        write_row_col(sheet, "RSVP", rsvp, reg_format, index)
        write_row_col(sheet, "side", side, reg_format, index)
        write_row_col(sheet, "group", group, reg_format, index)
        write_row_col(sheet, "couple", couple, reg_format, index)
        write_row_col(sheet, "date opened", date_opened, reg_format, index)
        write_row_col(sheet, "diet info", diet_info, reg_format, index)
        write_row_col(sheet, "needs a ride from", needs_ride_loc, reg_format, index)
        write_row_col(sheet, "can give a ride from", has_ride_loc, reg_format, index)
        write_row_col(sheet, "number of free seats", car_room, reg_format, index)
        write_row_col(sheet, "email", email, reg_format, index)
        write_row_col(sheet, "phone number", phone, reg_format, index)
        write_row_col(sheet, "message", message, reg_format, index)
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
        if col in {3, 4, 5, 7}:
            sheet["sheet"].set_column(col, col, 8)
        else:
            sheet["sheet"].set_column(col, col, 15)
    workbook.close()