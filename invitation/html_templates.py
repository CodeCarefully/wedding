__author__ = 'User'


initial_english_html = """
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/gavriela-prod/meer/Pictures/email.png"
        alt="Press on image to go to wedding invitation">
    </div>
    <br/>
    <br/>
    <p>Dear {0},</p>
    <br/>
    <p>We are happy to inform you that you are invited to Gavriel Lazan and Ariela Karp's Wedding!</p>
    <p>Please view Invitation and RSVP by clicking the link below:</p>
    <p><a href="{1}">{1}</a></p>
    <p>&nbsp;</p>
    <p>Hoping to see you there!</p>
    <p>Gavriel and Ariela</p>
    """
initial_hebrew_html = """
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/gavriela-prod/meer/Pictures/email.png"
        alt="Press on image to go to wedding invitation">
    </div>
    <br/>
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">שלום {},</p>
    <p style="direction: rtl; text-align: right;">אנו מתכבדים להזמינכם לחתונתם של גבריל לזן ואריאלה קרפ!</p>
    <p style="direction: rtl; text-align: right;">בבקשה תעיינו בהזמנה ותאשרו את הגעתכם בקישור הבא:&nbsp;</p>
    <p style="direction: rtl; text-align: right;">
    <a href="{}">{}</a></p>
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">נשמח לראותכם בשמחתינו!</p>
    <p style="direction: rtl; text-align: right;">גבריאל ואריאלה</p>
"""

html_templates = {
    "initial_hebrew": initial_hebrew_html,
    "initial_english": initial_english_html
}