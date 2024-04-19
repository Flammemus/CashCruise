import random
import time

def blackJack(betAmount, balance):

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = []
    usedCards = []

    dealerHand = []
    playerHand = []

    for suit in suits:
        for rank in ranks:
            card = f"{rank} of {suit}"
            deck.append(card)

    def getCard(whomHand, whomHandInt, amount):
        drawn_cards = random.sample(deck, amount)
        whomHand.extend(drawn_cards)
        usedCards.extend(drawn_cards)
        for card in drawn_cards:
            deck.remove(card)
            rank = int(card.split()[0])
            if rank == 11:  # If drawn card is an ace
                whomHandInt.append(11)  # Treat ace as 11 initially
            else:
                whomHandInt.append(rank)

        # Dynamically adjust ace value if hand total exceeds 21
        num_aces = whomHandInt.count(11)  # Count the number of aces in the hand
        while sum(whomHandInt) > 21 and num_aces > 0:
            for i in range(len(whomHandInt)):
                if whomHandInt[i] == 11:  # Check if the card is an ace
                    whomHandInt[i] = 1  # Treat ace as 1
                    num_aces -= 1  # Reduce the count of aces
                    break

    def result(winner, betAmount, balance):
        print(f"\n@*- You {winner} {betAmount}! -*@\n")

        if winner == "won":
            return betAmount
        elif winner == "lost":
            return -betAmount
        elif winner == "you win with blackjack":
            return betAmount / 2
        else:
            return 0

    def showDealerHands():
        print("\n--------------------")
        time.sleep(0.15)
        print("\nDealer's hand:\n")
        time.sleep(0.15)

        for card in dealerHand:
            print(card)
            time.sleep(0.15)

        print(f"\nAdds up to {sum(dealerHandInt)}")
        time.sleep(0.15)

    def showPlayerHands():
        print("\n--------------------\n")
        time.sleep(0.15)
        print("Your hand:\n")
        time.sleep(0.15)

        for card in playerHand:
            print(card)
            time.sleep(0.15)

        print(f"\nAdds up to {sum(playerHandInt)}")
        time.sleep(0.15)

    def showDealerHandsMin1():
        print("\n--------------------")
        time.sleep(0.15)
        print("\nDealer's hand:\n")
        time.sleep(0.15)

        for i in range(len(dealerHand) - 1):
            print(dealerHand[i])
            time.sleep(0.15)

    dealerHandInt = []
    playerHandInt = []

    getCard(dealerHand, dealerHandInt, 2)
    getCard(playerHand, playerHandInt, 2)

    showDealerHandsMin1()
    showPlayerHands()

    if sum(playerHandInt) == 21:
        if len(playerHandInt) == 2:
            return result("win with blackjack", betAmount, balance)

    gaming = True
    while gaming:

        print()
        action = input("hit or stand?: ")

        if action.lower() == "hit":
            getCard(playerHand, playerHandInt, 1)
            showDealerHandsMin1()
            time.sleep(1)
            showPlayerHands()

            if sum(playerHandInt) > 21:
                return result("lost", betAmount, balance)
            
            elif sum(dealerHandInt) > 21:
                return result("won", betAmount, balance)

        if action.lower() == "stand":

            showDealerHands()

            while sum(dealerHandInt) < 17:
                getCard(dealerHand, dealerHandInt, 1)
                showDealerHands()
                time.sleep(1)

            if sum(playerHandInt) > 21:
                return result("lost", betAmount, balance)
            elif sum(dealerHandInt) > 21:
                return result("won", betAmount, balance)
            elif sum(playerHandInt) == sum(dealerHandInt):
                return result("lost", betAmount, balance)
            elif sum(playerHandInt) > sum(dealerHandInt):
                return result("won", betAmount, balance)
            elif sum(playerHandInt) < sum(dealerHandInt):
                return result("lost", betAmount, balance)