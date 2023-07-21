import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from mysite.settings.base import SENDER_EMAIL, EMAIL_APP_PSK


def email_sender(request_data):
    sender_email = SENDER_EMAIL
    receiver_email = "ansari.amaan@outlook.com"
    password = EMAIL_APP_PSK

    message = MIMEMultipart("alternative")
    message["Subject"] = request_data.get('subject')
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    This is my Portfolio Website:
    amaanansari.pythonanywhere.com"""
    html = """\
    <html>
      <body>
        <p>{msg_body}<br><br>
           From:<br>{firstname} {lastname}<br>Email: {email}
        </p>
      </body>
    </html>
    """.format(
        msg_body=request_data.get('message'),
        firstname=request_data.get('firstname'),
        lastname=request_data.get('lastname'),
        email=request_data.get('email')
    )

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
