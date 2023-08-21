from Email import EmailWork
from typing import Any


def main():
    # у меня код не работал при запуске, но почистил его как смог
    login: str = 'login@gmail.com'  # login
    password: str = 'qwerty'  # password
    subject: str = 'Subject'  # subject

    a: EmailWork = EmailWork(login=login, password=password, subject=subject)

    recipients: list = ['vasya@email.com', 'petya@email.com']
    message: str = 'Message'
    header: Any = None

    a.send_message(recipients, message)
    a.receive_message(header=header)


if __name__ == '__main__':
    main()

# send message
# msg = MIMEMultipart()
# msg['From'] = l
# msg['To'] = ', '.join(recipients)
# msg['Subject'] = subject
# msg.attach(MIMEText(message))
#
# ms = smtplib.SMTP(GMAIL_SMTP, 587)
# # identify ourselves to smtp gmail client
# ms.ehlo()
# # secure our email with tls encryption
# ms.starttls()
# # re-identify ourselves as an encrypted connection
# ms.ehlo()
#
# ms.login(l, passwORD)
# ms.sendmail(l,
#             ms, msg.as_string())
#
# ms.quit()
# send end


# recieve
# mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
# mail.login(l, passwORD)
# mail.list()
# mail.select("inbox")
# criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
# result, data = mail.uid('search', None, criterion)
# assert data[0], 'There are no letters with current header'
# latest_email_uid = data[0].split()[-1]
# result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
# raw_email = data[0][1]
# email_message = email.message_from_string(raw_email)
# mail.logout()
# end recieve
