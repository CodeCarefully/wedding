__author__ = 'User'


initial_english_html = """
    <p>Hi {0},</p>
    <p>We are happy to inform you that you are invited to Avichai Marks and Devora Moskovitz's wedding!</p>
    <p>Please view the invitation and RSVP.</p>
    <br/>
    <p><a href="{1}">
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/devora-dev/static/email/Eng_envelope_with_stamp.jpg"
        alt="Press on image to go to wedding invitation">
    </div>
    </a></p>
    <p>&nbsp;</p>
    <p>Hoping to see you there!</p>
    <p>Avichai and Devora</p>
    <br/>
    <p><small>If you were unable to open the link please copy the following link to your browser: </small>
    <small><a href="{1}">{1}</a></small>
    </p>
    """
initial_hebrew_html = """
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">שלום {0},</p>
    <p style="direction: rtl; text-align: right;">אנו מתכבדים להזמינכם לחתונתם של אביחי מרקס ודבורה מוסקוביץ!</p>
    <p style="direction: rtl; text-align: right;">בבקשה תעיינו בהזמנה ותאשרו את הגעתכם&nbsp;</p>
    <p style="direction: rtl; text-align: right;">
    <p><a href="{1}">
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/devora-dev/static/email/He_envelope_with_stamp.jpg"
        alt="לחץ כאן כדי להיכנס להזמנה">
    </div>
    </a></p>
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">נשמח לראותכם בשמחתינו!</p>
    <p style="direction: rtl; text-align: right;">אביחי ודבורה</p>
    <br/>
    <p><small>אם הלינק לא נפתח, בבקשה תנסו להעתיק לתוך הדפדפן את הלינק הבא: </small>
    <small><a href="{1}">{1}</a></small>
    </p>
"""

html_templates = {
    "initial_hebrew": initial_hebrew_html,
    "initial_english": initial_english_html
}