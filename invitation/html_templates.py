__author__ = 'User'

couple = ["Eitan", "Estrella"]
couple_h = ["אסטריה", "איתן"]

initial_english_html = """
    <p>Hi {0},</p>
    <p>We are happy to inform you that you are invited to Eitan Har Oz and Estrella Ruas's wedding!</p>
    <p>Please click on the image to view the invitation and RSVP.</p>
    <br/>
    <p><a href="{1}">
    <div style="left-margin: 10%;">
    <img src="http://static.itisourwedding.com/Estrella-dev/static/email/Eng_envelope_with_stamp.jpg"
        alt="Press on image to go to wedding invitation">
    </div>
    </a></p>
    <p>&nbsp;</p>
    <p>Hoping to see you there!</p>
    <p>Eitan and Estrella</p>
    <br/>
    <p><small>If you were unable to open the link please copy the following link to your browser: </small>
    <small><a href="{1}">{1}</a></small>
    </p>
    """
initial_hebrew_html = """
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">שלום {0},</p>
    <p style="direction: rtl; text-align: right;">אנו מתכבדים להזמינכם לחתונתם של איתן הר עוז ואסטריה רואס!</p>
    <p style="direction: rtl; text-align: right;">בבקשה תלחצו על התמונה כדי לעיין בהזמנה ולאשר את הגעתכם.&nbsp;</p>
    <p style="direction: rtl; text-align: right;">
    <p><a href="{1}">
    <div style="direction: rtl; text-align: right;">
    <img src="http://static.itisourwedding.com/Estrella-dev/static/email/He_envelope_with_stamp.jpg"
        alt="לחץ כאן כדי להיכנס להזמנה">
    </div>
    </a></p>
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">נשמח לראותכם בשמחתינו!</p>
    <p style="direction: rtl; text-align: right;">איתן ואסטריה</p>
    <br/>
    <p style="direction: rtl; text-align: right;">
    <small>אם הלינק לא נפתח, בבקשה תנסו להעתיק לתוך הדפדפן את הלינק הבא: </small>
    <small><a href="{1}">{1}</a></small>
    </p>
"""

opened_reminder_english_html = """
    <p>Hi {0},</p>
    <p>We noticed you haven't responded to our invitation yet.</p>
    <p>Please click on the image to view the invitation and RSVP.</p>
    <br/>
    <p><a href="{1}">
    <div style="left-margin: 10%;">
    <img src="http://static.itisourwedding.com/Estrella-dev/static/email/Eng_envelope_with_stamp.jpg"
        alt="Press on image to go to wedding invitation">
    </div>
    </a></p>
    <p>&nbsp;</p>
    <p>Hoping to see you there!</p>
    <p>Eitan and Estrella</p>
    <br/>
    <p><small>If you were unable to open the link please copy the following link to your browser: </small>
    <small><a href="{1}">{1}</a></small>
    </p>
    """
opened_reminder_hebrew_html = """
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">שלום {0},</p>
    <p style="direction: rtl; text-align: right;">שמנו לב שלא אישרתם את הגעתכם לחתונה</p>
    <p style="direction: rtl; text-align: right;">בבקשה תלחצו על התמונה כדי לעיין בהזמנה ולאשר את הגעתכם.&nbsp;</p>
    <p style="direction: rtl; text-align: right;">
    <p><a href="{1}">
    <div style="direction: rtl; text-align: right;">
    <img src="http://static.itisourwedding.com/Estrella-dev/static/email/He_envelope_with_stamp.jpg"
        alt="לחץ כאן כדי להיכנס להזמנה">
    </div>
    </a></p>
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">נשמח לראותכם בשמחתינו!</p>
    <p style="direction: rtl; text-align: right;">איתן ואסטריה</p>
    <br/>
    <p style="direction: rtl; text-align: right;">
    <small>אם הלינק לא נפתח, בבקשה תנסו להעתיק לתוך הדפדפן את הלינק הבא: </small>
    <small><a href="{1}">{1}</a></small>
    </p>
"""


html_templates = {
    "initial_hebrew": initial_hebrew_html,
    "initial_english": initial_english_html,
    "opened_reminder_english": opened_reminder_english_html,
    "opened_reminder_hebrew": opened_reminder_hebrew_html
}