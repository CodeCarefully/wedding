__author__ = 'User'


initial_english_html = """
    <p>Hi {0},</p>
    <p>We are happy to inform you that you are invited to Avichai Marks and Devora Moskovitz's wedding!</p>
    <p>Please view Invitation and RSVP by clicking the link below:</p>
    <p><a href="avichaidevora.com/invitation/{1}">avichaidevora.com/invitation/{1}</a></p>
    <p>&nbsp;</p>
    <p>Hoping to see you there!</p>
    <p>Avichai and Devora</p>
    """
initial_hebrew_html = """
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">שלום {},</p>
    <p style="direction: rtl; text-align: right;">אנו מתכבדים להזמינכם לחתונתם של אביחי מרקס ודבורה מוסקוביץ!</p>
    <p style="direction: rtl; text-align: right;">בבקשה תעיינו בהזמנה ותאשרו את הגעתכם בקישור המצורף הבא&nbsp;</p>
    <p style="direction: rtl; text-align: right;">
    <a href="avichaidevora.com/invitation/{}">avichaidevora.com/invitation/{}</a></p>
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">נשמח לראותכם בשמחתינו!</p>
    <p style="direction: rtl; text-align: right;">אביחי ודבורה</p>
"""

html_templates = {
    "initial_hebrew": initial_hebrew_html,
    "initial_english": initial_english_html
}