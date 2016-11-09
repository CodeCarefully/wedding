__author__ = 'User'

from wedding.settings import DB_DIR
from invitation.html_templates import *
from sparkpost import SparkPost
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

KEY_FILE_NAME = DB_DIR + "/code.txt"

couple_email = "rsvp@streytanwedding.com"

def get_key():
  with open(KEY_FILE_NAME, 'r') as code_file:
      return code_file.readline().strip()

client = SparkPost(get_key())
def email_person(person, name, template):

    email = person.email
    sent_emails = 0
    if not email:
        return sent_emails

    # msg = MIMEMultipart()
    # msg["From"] = '{} and {}\'s wedding<{}>'.format(*(couple + [couple_email]))
    # msg['To'] = "{} <{}>".format(person.name(), email)
    # msg['Subject'] = get_subject(person, template)
    #
    # msg.attach(MIMEText(get_email_html(person, name, template), "html"))
    #
    # smtp = smtplib.SMTP("localhost")
    # errs = smtp.sendmail(couple_email, email, msg.as_string())
    # if not errs:
    #     sent_emails += 1
    # smtp.quit()

    try:
        message = {
            'from_email': '{} and {}\'s wedding<{}>'.format(*(couple + [couple_email])),
            'reply_to': couple_email,
            'html': get_email_html(person, name, template),
            'subject': get_subject(person, template),
            'recipients': [
                {
                    'address': {
                        'email': email,
                        'name': person.name()
                    }
                }
            ],
            'track_opens': True,
            "track_clicks": True
        }
        result = client.transmissions.send(**message)
        sent_emails += result["total_accepted_recipients"]
    except Exception as e:
        print('An email error occurred: %s - %s' % (e.__class__, e))
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
    if template in {'opened_reminder', "wedding_reminder"}:
        if is_english:
            subject = '{} and {}\'s wedding - Reminder'.format(*couple)
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

