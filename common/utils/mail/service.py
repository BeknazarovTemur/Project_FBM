import os

from common.const.messages import RESET_PASSWORD_SUBJECT, VERIFICATION_SUBJECT
from common.utils import get_random_string, redis_client
from common.utils.mail.email_service import send_email
from common.utils.mail.reset_password_code_page import HTML as RESET_PASSWORD_CODE_LINK
from common.utils.mail.reset_password_link_page import HTML as RESET_PASSWORD_LINK_PAGE
from common.utils.mail.verification_page import HTML as VERIFICATION_PAGE
from core.settings import REDIS_TIMEOUTS

host_url = os.environ.get("EMAIL_VERIFY_URL")
client_url = os.environ.get("CLIENT_URL")


def send_verification_email(user):
    url_string = get_random_string(25)

    redis_client.redis_set(url_string, str(user.uuid), REDIS_TIMEOUTS["verification_token"])

    verify_url = f"{host_url}{url_string}/"
    body = VERIFICATION_PAGE.replace("URL", verify_url)

    send_email(
        VERIFICATION_SUBJECT,
        body,
        [user.email],
    )


def send_reset_password_code_mail(user):
    code = get_random_string(5)

    redis_client.redis_set(
        f"reset-password-{user.email}", code, REDIS_TIMEOUTS["reset_password"]
    )

    body = RESET_PASSWORD_CODE_LINK.replace("RESET_PASSWORD_CODE", code)

    send_email(
        RESET_PASSWORD_SUBJECT,
        body,
        [user.email],
    )


def send_reset_password_link_email(user):
    code = get_random_string(5)

    redis_client.redis_set(
        f"reset-password-{user.email}", code, REDIS_TIMEOUTS["reset_password"]
    )

    reset_password_url = f"{client_url}?code={code}&email={user.email}"
    body = RESET_PASSWORD_LINK_PAGE.replace("RESET_PASSWORD_LINK", reset_password_url)

    send_email(
        RESET_PASSWORD_SUBJECT,
        body,
        [user.email],
    )
