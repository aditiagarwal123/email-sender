import sys
import os
import re
from smtplib import SMTP_SSL as SMTP       
from email.mime.text import MIMEText

SMTPserver = 'smtp.gmail.com'
sender =     input("Enter sender's email address:")
destination = input("Enter receiver's email address:")
password = input("Enter your password:")

text_subtype = 'plain'
content=input("Enter message:")
subject="Sent from Python"

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']= subject
    msg['From']   = sender              

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(sender, password)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except:
    sys.exit( "mail failed; %s" % "CUSTOM_ERROR" )
