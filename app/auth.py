
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.db_settings import execute_query
import random


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


def  Register():
    try:
        full_name = input("Enter your full name: ")
        email = input("Enter your email: ")

        email_query = "SELECT email FROM users;"
        e_list = execute_query(query=email_query, fetch="all")
        
        for list in e_list:
            if list[0] == email:
                print("This email already exists!")
                return

        code = random.randint(1000, 9999)

        message = f"Sizning tasdiqlash kodingiz: {code}!"
        email_sender(r_email=email, m_body=message )
        in_code = input("Enter register code (we send it to your email): ")
        
        while int(code) != int(in_code):
            in_code = input("Enter register code (we send it to your email): ")


        register_query = "INSERT INTO users (full_name, email, is_login) VALUES (%s, %s, %s);"

        execute_query(query=register_query, params=(full_name, email, True))
        print("Register successfully")
        
    
    except BaseException as e:
        print(e)    




def logout():
    logout_query = "UPDATE  users SET is_login = FALSE;"

    execute_query(query=logout_query)


admin_email = "admin@gmail.com"



def login():
    email = input("Enter your email: ")

    if email == admin_email:
        return "admin"
    
    email_query = "SELECT email FROM users;"
    e_list = execute_query(query=email_query, fetch="all")
    
    for list in e_list:
        if list[0] == email:
            login_query = "UPDATE users SET is_login = TRUE WHERE email = %s;"
            execute_query(query=login_query, params=(email,))
            return "user"
        

