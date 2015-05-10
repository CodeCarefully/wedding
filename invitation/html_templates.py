__author__ = 'User'


initial_english_html = """

    <br/>
    <p>Hey {0},</p>
    <br/>
    <a href="{1}">
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/gavriela-prod/meer/Pictures/email.png"
        alt="Press on image to go to wedding invitation">
    </div>
    </a>
    <br/>
    <p>We're getting married - and we'd love for you to come and celebrate with us!</p>
    <p>Click the image or on the link below to see the invitation and RSVP. </p>
    <p><a href="{1}">{1}</a></p>
    <p>&nbsp;</p>
    <p>Hope to see you there!</p>
    <p>Gavi and Ariela</p>
    """
initial_hebrew_html = """
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">היי {0},</p>
    <br/>
    <a href="{1}">
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/gavriela-prod/meer/Pictures/email.png"
        alt="לחצו על התמונה כדי לפתוח את ההזמנה">
    </div>
    </a>
    <br/>
    <p style="direction: rtl; text-align: right;">אנחנו מתחתנים - ונשמח שתבואו לחגוג איתנו!</p>
    <p style="direction: rtl; text-align: right;">לחצו על התמונה או על הקישור למטה כדי לראות את ההזמנה ולאשר את הגעתכם.</p>
    <p style="direction: rtl; text-align: right;">
    <a href="{1}">{1}</a></p>
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">מצפים לראותכם!</p>
    <p style="direction: rtl; text-align: right;">גבריאל ואריאלה</p>
"""


opened_reminder_english_html = """

    <br/>
    <p>Hey {0},</p>
    <br/>
    <a href="{1}">
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/gavriela-prod/meer/Pictures/email.png"
        alt="Press on image to go to wedding invitation">
    </div>
    </a>
    <br/>
    <p>We notice that you haven't responded to our invitation. </p>
    <p>Please let us know by May 15th if you'll be able to come and celebrate with us!</p>
    <p>Click the image or on the link below to see the wedding invitation and RSVP. </p>
    <p><a href="{1}">{1}</a></p>
    <p>&nbsp;</p>
    <p>Hope to see you there!</p>
    <p>Gavi and Ariela</p>
    """

opened_reminder_hebrew_html = """
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">היי {0},</p>
    <br/>
    <a href="{1}">
    <div style="text-align:center;">
    <img src="http://static.itisourwedding.com/gavriela-prod/meer/Pictures/email.png"
        alt="לחצו על התמונה כדי לפתוח את ההזמנה">
    </div>
    </a>
    <br/>
    <p style="direction: rtl; text-align: right;">שמנו לב שלא אישרתם את הגעתכם לחתונה - ונשמח אם תבואו לחגוג איתנו!</p>
    <p style="direction: rtl; text-align: right;">אז אנא אשרו הגעה/אי הגעה עד ל-15.5 ע"י לחיצה על התמונה או על הקישור למטה.</p>
    <p style="direction: rtl; text-align: right;">
    <a href="{1}">{1}</a></p>
    <p style="direction: rtl; text-align: right;">&nbsp;</p>
    <p style="direction: rtl; text-align: right;">מצפים לראותכם!</p>
    <p style="direction: rtl; text-align: right;">גבריאל ואריאלה</p>
"""


html_templates = {
    "initial_hebrew": initial_hebrew_html,
    "initial_english": initial_english_html,
    "opened_reminder_english": opened_reminder_english_html,
    "opened_reminder_hebrew": opened_reminder_hebrew_html
}