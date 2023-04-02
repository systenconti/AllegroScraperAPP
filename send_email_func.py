import smtplib
import ssl
from credentials import username, password
from email.message import EmailMessage


def send_email():
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    msg = EmailMessage()
    msg['Subject'] = 'Najtańsze karmy Alpha Spirit na allegro'
    # me == the sender's email address
    # family = the list of all recipients' email addresses
    msg['From'] = username
    msg['To'] = "xiheartmakeup@gmail.com"
    msg.set_content('Lista karmy Alpha Spirit od najtańszych poniżej')

    with open("karmy.png", "rb") as img:
        img_data = img.read()
    msg.add_attachment(img_data, maintype='image',
                       subtype='png', filename='karmy.png')

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg=msg)


if __name__ == "__main__":
    send_email()
