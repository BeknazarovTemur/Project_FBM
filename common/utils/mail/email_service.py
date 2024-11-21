import smtplib
import threading
from email.mime.text import MIMEText

from core.settings import MAIL_CONFIG



_sender = MAIL_CONFIG["email_host_user"]
_password = MAIL_CONFIG["email_host_password"]
_host = MAIL_CONFIG["email_host_password"]
_port = MAIL_CONFIG["email_port"]


def send_email(subject, body, recipients):
    threading.Thread(target=_send_mail, args=(subject, body, recipients)).start()


def _send_mail(subject, body, recipients):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = _sender
    msg["To"] = ", ".join(recipients)
    with smtplib.SMTP(_host, _port) as server:
        server.starttls()
        server.login(_sender, _password)
        server.sendmail(_sender, recipients, msg.as_string())
