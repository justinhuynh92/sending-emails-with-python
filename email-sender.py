import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Justin Huynh'
email['to'] = 'justinhuynh855@gmail.com'
email['subject'] = 'you won a millie'

email.set_content('i am a boss')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('justinhuynh855@gmail.com', 'J060692h')
    smtp.send_message(email)
    print('all good boss')
