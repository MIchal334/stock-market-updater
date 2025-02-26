import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv

from application.port.outbound.user_informer import UserInformer

SENDER_EMAIL = getenv("SENDER_EMAIL", "email@gmail.com")
SENDER_PASSWORD = getenv("SENDER_PASSWORD", "password")
EMAIL_TOPIC = "Market stock info"


class EmailUserInformer(UserInformer):

    def send_info_to_user(self, user_email: str, info: str) -> None:
        msg = self.__message_creator(user_email=user_email, info=info)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()  #
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, user_email, msg.as_string())
            server.quit()
        except Exception as e:
            print(f"{e}")

    @staticmethod
    def __message_creator(user_email: str, info: str) -> MIMEMultipart:
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = user_email
        message["Subject"] = EMAIL_TOPIC
        message.attach(MIMEText(info, "plain"))
        return message
