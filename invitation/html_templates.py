__author__ = 'User'


initial_english_html = """

    <br/>
    <p>Dear {0},</p>
    <br/>
    <a href="{1}">
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/gavriela-prod/meer/Pictures/email.png"
        alt="Press on image to go to wedding invitation">
    </div>
    </a>
    <br/>
    <p>We are happy to inform you that you are invited to our wedding!</p>
    <p>Please view invitation and RSVP by clicking the image or the link below:</p>
    <p><a href="{1}">{1}</a></p>
    <p>&nbsp;</p>
    <p>Hoping to see you there!</p>
    <p>Gavriel and Ariela</p>
    """
initial_hebrew_html = """
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">שלום {0},</p>
    <br/>
    <a href="{1}">
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/gavriela-prod/meer/Pictures/email.png"
        alt="Press on image to go to wedding invitation">
    </div>
    </a>
    <br/>
    <p style="direction: rtl; text-align: right;">אנו מתכבדים להזמינכם לחתונתנו, לחצו על התמונה או הקישור המצורף בכדי לצפות בהזמנה ולאשר הגעה:</p>
    <p style="direction: rtl; text-align: right;">
    <a href="{1}">{1}</a></p>
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">נשמח לראותכם בשמחתינו!</p>
    <p style="direction: rtl; text-align: right;">גבריאל ואריאלה</p>
"""

html_templates = {
    "initial_hebrew": initial_hebrew_html,
    "initial_english": initial_english_html
}