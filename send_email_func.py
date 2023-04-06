import smtplib
import ssl
from credentials import username, password
from email.message import EmailMessage


offers = [['Karma AS WILD FISH 12kg only bez zbóż rybna sucha', 'https://allegro.pl/oferta/karma-as-wild-fish-12kg-only-bez-zboz-rybna-sucha-10220232459', '235,45 zł'],
          ['Alpha Spirit Wild Fish ryby półwilgotna karma 12kg',
              'https://allegro.pl/oferta/alpha-spirit-wild-fish-ryby-polwilgotna-karma-12kg-9956784790', '236,99 zł'],
          ['Alpha Spirit Wild Fish 12kg RYBY',
              'https://allegro.pl/oferta/alpha-spirit-wild-fish-12kg-ryby-9926782116', '238,60 zł']]


def send_email(list_of_offers):
    offers = ""
    for offer in list_of_offers:
        offers += str(offer) + "\n"
    offers = offers.replace("[", "").replace("]","")

    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    msg = EmailMessage()
    msg['Subject'] = 'Najtańsze karmy Alpha Spirit na allegro'
    # me == the sender's email address
    # family = the list of all recipients' email addresses
    msg['From'] = username
    msg['To'] = "xiheartmakeup@gmail.com"
    msg.set_content(f'Lista najtańszych 10 pozycji karmy Alpha Spirit poniżej\n{offers}')

    with open("karmy.png", "rb") as img:
        img_data = img.read()
    msg.add_attachment(img_data, maintype='image',
                       subtype='png', filename='karmy.png')

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg=msg)
    print("Email was sent.")


if __name__ == "__main__":
    send_email(offers)
