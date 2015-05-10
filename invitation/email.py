__author__ = 'User'
import mandrill
from wedding.settings import DB_DIR
from invitation.html_templates import html_templates
from invitation.export import make_couple_name

KEY_FILE_NAME = DB_DIR + "/code.txt"
HEBREW_SUBJECT = "הזמנה לחתונה של גבריאל לזן ואריאלה קארפ"
ENGLISH_SUBJECT = 'Gavriel Lazan and Ariela Karp\'s Wedding Invitation!'


def get_key():
    with open(KEY_FILE_NAME, 'r') as code_file:
        return code_file.readline().strip()


def email_person(invite, emails, name, template):
    emails_sent = 0
    no_emails = True
    for email in emails:
        if email:
            no_emails = False
    if no_emails:
        return emails_sent
    try:
        mandrill_client = mandrill.Mandrill(get_key())
        message = {
            'auto_html': None,
            'auto_text': True,
            'from_email': 'gavrielawedding@gmail.com',
            'from_name': 'Gavriel Lazan and Ariela Karp',
            'headers': {'Reply-To': 'gavrielawedding@gmail.com'},
            'html': get_email_html(invite, name, template),
            'important': True,
            'inline_css': None,
            'subject': get_subject(invite, template),
            'tags': ['initial invitation'],
            'to': [{'email': email,
                    'type': 'to'} for email in emails if email],
            'view_content_link': None
        }
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
        for result_dict in result:
            if 'status' in result_dict and result_dict['status'] == 'sent':
                emails_sent += 1

    except mandrill.Error as e:
        # Mandrill errors are thrown as exceptions
        #print('A mandrill error occurred: %s - %s' % (e.__class__, e))
        # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'
        raise
    return emails_sent


def get_subject(invite, template):
    is_english = invite.is_english()
    if template in {'initial', 'not_opened_reminder'}:
        if is_english:
            subject = ENGLISH_SUBJECT
        else:
            subject = HEBREW_SUBJECT
    if template in {'opened_reminder'}:
        if is_english:
            subject = ENGLISH_SUBJECT + ' - Reminder'
        else:
            subject = HEBREW_SUBJECT + " - תזכורת"
    return subject


def email_invite(invite, template):
    guest_list = invite.person_list()
    i = 0
    emails_sent = 0
    while i < len(guest_list):
        if invite.couple and i == 0 and not invite.has_guest_person() and len(guest_list) > 1:
            person0 = guest_list[0]
            person1 = guest_list[1]
            emails = [person0.email_internal_use, person1.email_internal_use]
            and_text = " and "
            if not invite.is_english():
                and_text = " ו"
            name = make_couple_name(person0, person1, and_text)
            emails_sent += email_person(invite, emails, name, template)
            i += 2
        else:
            person = guest_list[i]
            emails_sent += email_person(invite, [person.email_internal_use], person.name, template)
            i += 1
    return emails_sent


def get_email_html(invite, name, template):
    is_english = invite.is_english()
    url = invite.invitation_url()
    english_html = html_templates[template + "_english"].format(name, url)
    hebrew_html = html_templates[template + "_hebrew"].format(name, url, url)
    if is_english:
        html = english_html
    else:
        html = hebrew_html
    return html

