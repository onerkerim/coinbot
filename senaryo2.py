from datetime import datetime
import time
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_emails(title,msg):
    mail_content = msg
    #The mail addresses and password
    sender_address = 'pyhonmailgonder@gmail.com'
    sender_pass = '02120212Oner'
    receiver_address = 'onerkerim@me.com'
    try:
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = title
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
    except Exception as e:
        print(e)

while True:
    now = datetime.now().strftime("%H:%M:%S")
    #Hedef saatleri kendine göre belirle
    #if (now == '14:00:00'):
    #    os.system("py script1.py")
    #elif (now == '15:00:00'):
    #    os.system("py script2.py")
    #elif (now == '16:00:00'):
    #    os.system("py script3.py")
    print(now)
    send_emails("Background code run",now+" saatinden gönderildi")

    time.sleep(180)
