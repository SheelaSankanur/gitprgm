import smtplib
from email.mime.text import MIMEText

sender_mail="sender@gmail.com"
receiver_mail="receiver@gmail.com"
app_sender_password="1245367897894"

subject="writing a mail in python"
body="fdkfncm cjsncsa  jnkjd msnkjdhsjand jdskjdnsamd "

msg=MIMEText[body]
msg["subject"]=subject
msg["sender"]=sender_mail
msg["receiver"]=receiver_mail

while smtplib.SMTP("smtp.office365.com",587) as smtp:
    smtp.startlist()
    smtp.login(sender_mail,app_sender_password)
    smtp.send(msg)