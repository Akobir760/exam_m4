
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def email_sender(r_email, m_body):
    sender_email = "sanjarbekwork@gmail.com"
    receiver_email = r_email
    password = "pqmk cvds dzdn gmll"

    subject = "Test Email"
    body = m_body

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)

    except Exception as e:
        print(f"Failed to send email. Error: {e}")
