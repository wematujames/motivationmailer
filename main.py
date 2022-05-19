from quotes import QuotesManager
from mail_manager import MailManager
import datetime as dt

DAY = 0 # Motivational quote to be sent on Mondays

# Instances
mail = MailManager()
quotes = QuotesManager()


today = dt.datetime.now()
if today.weekday() == DAY:
    quote = quotes.select_quote()
    mail.send_mail(quote)


        
