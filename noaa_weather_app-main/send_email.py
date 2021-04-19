import os

import smtplib

from email.message import EmailMessage

email_account = os.environ.get('EMAIL')
email_password = os.environ.get('GmailPassWord')


msg = EmailMessage()
msg['Subject'] = 'Weather Update for the next 3 days'
msg['From'] = email_account
msg['To'] = 'a.olaoye1@gmail.com'
msg.set_content('weather for the next 3 days attached')


with open('2021-04-06.csv','rb') as f:
    file_data = f.read()
    file_name = f.name
    
#attach file
msg.add_attachment(file_data,maintype='application',subtype = 'octet-stream',filename=file_name)


#mail server connection
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	
	smtp.login(email_account, email_password)

	smtp.send_message(msg)



