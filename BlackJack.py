############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random

# cards array temp initialize
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def generateCard():
    return random.choice(cards)

def sumCards(player) -> int:
    if sum(player) == 21 and len(player) == 2:
        return 0  # Blackjack
    while 11 in player and sum(player) > 21:
        player.remove(11)
        player.append(1)
    return sum(player)

def compare(dealer, player):
    user_score = sumCards(player)
    computer_score = sumCards(dealer)
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose "
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack "
    elif user_score > 21:
        return "You went over. You lose "
    elif computer_score > 21:
        return "Opponent went over. You win "
    elif user_score > computer_score:
        return "You win "
    else:
        return "You lose "

def startGameMain(dealer: list, player: list):
    # deal 2 cards each
    for _ in range(2):
        dealer.append(generateCard())
        player.append(generateCard())

    gameOver = False
    while not gameOver:
        user_score = sumCards(player)
        computer_score = sumCards(dealer)
        print(f"   Your cards: {player}, current score: {user_score}")
        print(f"   Computer's first card: {dealer[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            gameOver = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player.append(generateCard())
            else:
                gameOver = True

    while computer_score != 0 and computer_score < 17:
        dealer.append(generateCard())
        computer_score = sumCards(dealer)

    print(f"   Your final hand: {player}, final score: {user_score}")
    print(f"   Computer's final hand: {dealer}, final score: {computer_score}")
    print(compare(dealer, player))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print(logo)
    startGameMain([], [])
