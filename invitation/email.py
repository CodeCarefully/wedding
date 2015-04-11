__author__ = 'User'
import mandrill
from wedding.settings import DB_DIR
from invitation.html_templates import html_templates

KEY_FILE_NAME = DB_DIR + "\\code.txt"


def get_key():
    with open(KEY_FILE_NAME, 'r') as code_file:
        return code_file.readline().strip()


def email_person(person, template):
    if not person.email:
        return
    try:
        mandrill_client = mandrill.Mandrill(get_key())
        message = {
            'auto_html': None,
            'auto_text': True,
            'from_email': 'gavrielawedding@gmail.com',
            'from_name': 'Avichai and Devora\'s wedding',
            'headers': {'Reply-To': 'gavrielawedding@gmail.com'},
            'html': get_email_html(person, template),
            'important': True,
            'inline_css': None,
            'subject': 'Avichai and Devora\'s wedding Invitation!',
            'tags': ['password-resets'],
            'to': [{'email': person.email,
                    'name': person.name(),
                    'type': 'to'}],
            'view_content_link': None
        }
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
        # log result

    except mandrill.Error as e:
        # Mandrill errors are thrown as exceptions
        print('A mandrill error occurred: %s - %s' % (e.__class__, e))
        # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'
        raise


def get_email_html(person, template):
    is_english = person.invitation.is_english()
    invitation_id = person.invitation.invite_id
    english_html = html_templates[template + "_english"].format(person.english_name, invitation_id)
    hebrew_html = html_templates[template + "_hebrew"].format(person.hebrew_name, invitation_id, invitation_id)
    if is_english:
        html = english_html
    else:
        html = hebrew_html
    return html

