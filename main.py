import random
import smtplib
import datetime as dt
import os


EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO_EMAIL_ADDR = os.environ["TO_EMAIL_ADDR"]

def select_quote ():
    try:
        with open("quotes.txt") as quotes:
            quotes_list = quotes.readlines()
    except FileNotFoundError:
        print("Opps. No quotes file found")
    except:
        print("error occured")
    else:
        selected_quote = quotes_list[random.randint(0, len(quotes_list) - 1)].strip().split(" - ")
        return selected_quote


def is_day_to_send(day = 0):
    now = dt.datetime.now()
    if now.weekday() == day:
        return True
    return False


def send_mail():
    if is_day_to_send():
        quote = select_quote()
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=EMAIL, password=PASSWORD)
            conn.sendmail(
                to_addrs= TO_EMAIL_ADDR, 
                from_addr=EMAIL, 
                msg=f"Subject:Motivational Quote\n\n{quote[0]} \n- by {quote[1]}"
                )
send_mail()
        
