import smtplib
import json
from email.message import EmailMessage


json_file = open("config.json")
gmail_cfg = json.load(json_file)

print(gmail_cfg)


msg = EmailMessage()
msg["to"] = gmail_cfg["email"]
msg["from"] = gmail_cfg["email"]
msg["Subject"] = "test de mail"
msg.set_content('envoie du mail')


with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port" ])as smtp :
    smtp.login (gmail_cfg["email"],gmail_cfg["pwd" ])
    smtp.send_message(msg)
    print ("Email sent | ")
