import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Binny'    # name of person who send email
email['to'] = 'bb@gmail.com'    # give to email id
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('xyz@gmail.com', 'asjdjjnsndjshdbshjbbds') # give gmail login username and password
    smtp.send_message(email)
    print('all good boss!')