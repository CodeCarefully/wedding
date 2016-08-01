__author__ = 'User'
import mandrill
from wedding.settings import DB_DIR
from invitation.html_templates import *

KEY_FILE_NAME = DB_DIR + "/code.txt"

couple_email = "streytan@gmail.com"

def get_key():
    with open(KEY_FILE_NAME, 'r') as code_file:
        return code_file.readline().strip()


def email_person(person, name, template):
    email = person.email
    sent_emails = 0
    if not email:
        return sent_emails
    try:
        mandrill_client = mandrill.Mandrill(get_key())
        message = {
            'auto_html': None,
            'auto_text': True,
            'from_email': couple_email,
            'from_name': '{} and {}\'s wedding'.format(*couple),
            'headers': {'Reply-To': couple_email},
            'html': get_email_html(person, name, template),
            'important': True,
            'inline_css': None,
            'subject': get_subject(person, template),
            'tags': ['password-resets'],
            'to': [{'email': email,
                    'name': person.name(),
                    'type': 'to'}],
            'view_content_link': None
        }
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
        for result_dict in result:
            if result_dict['status'] == 'sent':
                sent_emails += 1

    except mandrill.Error as e:
        # Mandrill errors are thrown as exceptions
        print('A mandrill error occurred: %s - %s' % (e.__class__, e))
        # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'
        raise

    return sent_emails


def get_subject(person, template):
    invite = person.invitation
    is_english = invite.is_english()
    subject = ""
    if template in {'initial', 'not_opened_reminder'}:
        if is_english:
            subject = '{} and {}\'s wedding Invitation!'.format(*couple)
        else:
            subject = "הזמנה לחתונה של {} ו{}".format(*couple_h)
    if template in {'opened_reminder'}:
        if is_english:
            subject = '{} and {}\'s wedding Invitation - Reminder'.format(*couple)
        else:
            subject = "הזמנה לחתונה של {} ו{} - תזכורת".format(*couple_h)
    return subject


def get_email_html(person, name, template):
    invite = person.invitation
    is_english = invite.is_english()
    url = invite.invitation_url()
    english_html = html_templates[template + "_english"].format(name, url)
    hebrew_html = html_templates[template + "_hebrew"].format(name, url)
    if is_english:
        html = english_html
    else:
        html = hebrew_html
    return html

