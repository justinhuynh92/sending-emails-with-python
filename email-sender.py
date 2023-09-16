import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Justin Huynh'
email['to'] = 'justinhuynh855@gmail.com'
email['subject'] = 'you won a millie'

email.set_content(html.substitute({'name': 'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('justinhuynh855@gmail.com', 'J060692h')
    smtp.send_message(email)
    print('all good boss')
