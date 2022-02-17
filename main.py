import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

smpt_host = os.environ['SMTP_HOST']
sender = os.environ['SMTP_ACCOUNT']
sender_pass = os.environ['SMTP_PASSWORD']
recipient = os.environ['SMTP_RECEIVER']
body = "A test email from Python"
subject = "ΦΟΒΟΣ"

msg = MIMEMultipart('alternative')

msg['From'] = sender
msg['To'] = recipient
msg['subject'] = subject

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)

try:
    # I have non-ascii in my hostname. `local_hostname` required for me.
    mailserver = smtplib.SMTP(smpt_host, 587, local_hostname='woof@local')
    # mailserver.set_debuglevel(True)
    mailserver.starttls()
    mailserver.login(sender, sender_pass)
    mailserver.send_message(msg)

    # Was receiving this exception prior to setting `local_hostname` above
except UnicodeEncodeError:
    print("UnicodeEncodeError\n")
    print(msg)
else:
    print("Message sent.")
finally:
    mailserver.quit()
