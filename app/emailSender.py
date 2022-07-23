import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv


def send_mail(content):
    load_dotenv()
    # to set the password and sender email create a .env file and follow the .env.example file
    # allow 2 authentifications factors
    msg = EmailMessage()
    password = os.getenv("EMAIL_PASSWORD")
    msg['From'] = os.getenv("EMAIL_ADRESS")
    msg.set_content(content)
    msg['Subject'] = 'Daily report'
    # put the receive email adress
    msg['To'] = "wissem22111@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg["from"], password)
    print("logged")
    server.send_message(msg)


send_mail("aa")
