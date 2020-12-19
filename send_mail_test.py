import os
import smtplib
import imghdr
from email.message import EmailMessage # To Format email handle more cleaningly

usremail = os.environ.get('useremail')
password = os.environ.get('userpass')
to = "youremail@domain.com"

msg = EmailMessage()
msg['Subject'] = "My Crush"
msg['From'] = usremail
msg['To'] = to
msg.set_content('I love her very much!!!')

with open('testImage.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp: Need ehlo and starttls
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
# with smtplib.SMTP('localhost', 1025) as smtp: # This is for Email Handelling locally so ehlo, starttsl and login are disabled For CMD: py -m smtpd -c DebuggingServer -n localhost:1025
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    smtp.login(usremail, password)
    # subject = "This Subject" When using EmailMessage class
    # body = "Hello World!"
    # message = f"Subject: {subject}\n\n {body}"
    smtp.send_message(msg)
    # smtp.sendmail(usremail, '', message)
