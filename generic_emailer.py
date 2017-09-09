#!python3
#emailer.py is a simple script for sending emails using smtplib
#The idea is to assign a web-scraped file to the DATA_FILE constant.
#The data in the file is then read in and sent as the body of the email.

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email_list import EMAILS

DATA_FILE = 'data'
from_addr = 'your_email@gmail.com'
to_addr = 'your_email@gmail.com'  #Or any generic email you want all recipients to see
bcc = EMAILS

def create_message():
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Subject Line'
    return msg


def add_body_text(msg):
    with open(DATA_FILE) as f:
        body = f.read()
    msg.attach(MIMEText(body, 'plain'))
    return msg

def send_email(msg):
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587) #Specify Gmail Mail server
    smtp_server.ehlo() #Send mandatory 'hello' message to SMTP server
    smtp_server.starttls() #Start TLS Encryption as we're not using SSL.
    smtp_server.login(' your_email@gmail.com ', ' GMAIL APPLICATION ID ')
    text = msg.as_string()
    smtp_server.sendmail(from_addr, [to_addr] + bcc, text) 
    smtp_server.quit()

def main():
    header = create_message()
    msg = add_body_text(header)
    send_email(msg)

if __name__ == "__main__":
   main()
