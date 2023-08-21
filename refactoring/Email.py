import email
import smtplib
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# from email.MIMEText import MIMEText
# from email.MIMEMultipart import MIMEMultipart

class EmailWork:
    GMAIL_SMTP: str = "smtp.gmail.com"
    GMAIL_IMAP: str = "imap.gmail.com"

    def __init__(self, login: str, password: str, subject: str) -> None:
        self.login: str = login
        self.__password: str = password
        self.subject: str = subject

    def send_message(self, recipients: list, message: str) -> None:
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(EmailWork.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.__password)
        ms.sendmail(self.login, ms, msg.as_string())

        ms.quit()

    def receive_message(self, header) -> None:
        expected: str = 'There are no letters with current header'
        header_subject: str = f'(HEADER Subject "{header}")'

        mail = imaplib.IMAP4_SSL(EmailWork.GMAIL_IMAP)
        mail.login(self.login, self.__password)
        mail.list()
        mail.select("inbox")
        criterion = header_subject % header if header else 'ALL'

        result, data = mail.uid('search', None, criterion)
        assert data[0], expected

        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email.message_from_string(raw_email)
        mail.logout()
