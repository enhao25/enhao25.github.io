import smtplib

FROM = 'larloller@gmail.com'

TO = ["larloller@gmail.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "This message was sent with Python's smtplib."

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('larloller@gmail.com', 'Kingkong1')
server.sendmail(FROM, TO, message)
server.quit()