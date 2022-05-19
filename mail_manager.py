import os
import smtplib
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO_EMAIL_ADDR = os.environ["TO_EMAIL_ADDR"]

class MailManager ():
    def __init__(self) -> None:
        pass
    
    
    def send_mail(self, quote: str) -> None:
        quote = quote
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            conn.sendmail(
                to_addrs= TO_EMAIL_ADDR, 
                from_addr=EMAIL, 
                msg=f"Subject:Motivational Quote\n\n{quote[0]} \n- by {quote[1]}"
                )