import random

class QuotesManager ():
    def __init__(self) -> None:
        pass
    
    def select_quote (self) -> str:
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