import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from login import login
from rules import *

from art import *
from blackjack import *
from roulette import *
from coinflip import *

cred = credentials.Certificate("cashcruiseKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def getBalance(doc_ref):
    if doc_ref is not None:
        balance_doc = doc_ref.get()
        if balance_doc.exists:
            return balance_doc.to_dict().get("Balance")
        else:
            print("Balance document does not exist.")
            return None
    else:
        print("No account logged in.")
        doc_ref, accountName = login(db)
        return None
    
def updateBalance(newBalance, doc_ref):
    if doc_ref is not None:
        doc_ref.update({"Balance": newBalance})

    else:
        print("No account logged in.")

doc_ref, accountName = login(db)

if accountName is not None:
    pass
else:
    print("Login failed. Please try again")

games = ["blackjack", "roulette", "coinflip"]
commands = ["bal          = Display current balance",
            "save         = Save progress to server",
            "'game' rules = Display rules for selected game"]
    
balance = getBalance(doc_ref)

if balance is None:
    balance = 100

def introduction():
    print("Here are the available commands:\n")

    for i in commands:
        print("-", i)

    print("\nHave a peek at our arsenal of games:\n")
    for i in games:
        print("-", i)
    print("\nType the name of a game to play it!\n")

    print(f"Your wallet: {balance}\n")

tprint("Cash Cruise!")
print("A p2w service!\n")
introduction()

gameloop = True
while gameloop:
 
    action = input(": ")

    def playGame(gameName, gameFunction, balance):
        gaming = True
        while gaming:
            enteringBetAmount = True
            while enteringBetAmount:
                bet_amount = input(f"Bet amount? (current bal: {balance} | 'Back' to return): ")
                
                if bet_amount.lower() == 'back':
                    print("\nGoing back to menu\n")
                    print("------------------\n")
                    introduction()
                    gaming = False
                    enteringBetAmount = False
                else:
                    try:
                        bet_amount = int(bet_amount)
                        if bet_amount > balance:
                            print("\nCan't bet more than you have\n")
                        else:
                            balance += gameFunction(bet_amount, balance)
                            updateBalance(balance, doc_ref)
                            enteringBetAmount = False
                    except ValueError:
                        print("Invalid input. Please enter a valid number or 'Back' to return to the menu.")
                    
        return balance

    

    if action.lower() == "blackjack":
        balance = playGame("Blackjack", blackJack, balance)
        
    elif action.lower() == "roulette":
        balance = playGame("Roulette", roulette, balance)

    elif action.lower() == "coinflip":
        balance = playGame("Coinflip", coinflip, balance)

    elif action.lower() == "save":
        updateBalance(balance, doc_ref)
        print("Saved successfully")

    elif action.lower() == "bal":
        print(f"Your balance: {balance}")

    elif action.lower() == "resetbal":
        balance = 0
    
    elif action.lower() == "give":
        print("Alright little party pooper, heres some pocket change..")
        balance = balance + 5000
    
    elif action.lower() == "coinflip rules":
        coinflipRules()
    
    elif action.lower() == "blackjack rules":
        blackjackRules()