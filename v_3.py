
import random

# Deck
cardfaces = []
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
royals = ["J", "Q", "K", "A"]
deck = []

for i in range(2, 11):
    cardfaces.append(str(i))
for j in range(4):
    cardfaces.append(royals[j])

for k in range(4):
    for l in range(13):
        card = cardfaces[l] + " of " + suits[k]
        deck.append(card)

# 6 random cards
game_cards = random.sample(deck, k=6)
first_chars = []
card_values = []

#creat list of 1st letter (proxy for value)
for m in game_cards:
    first_chars.append(m[0])

#convert to integer value
for n in first_chars:
    if n == str("A"):
        card_values.append(int(1))
    elif n == str("K") or n == str("Q") or n == str("J") or n == str("1"):
        card_values.append(int(0))
    else:
     card_values.append(int(n))

#Calc Score
player_score = 0
banker_score = 0
player_score += card_values[0]
player_score += card_values[1]
banker_score += card_values[2]
banker_score += card_values[3]

#function - reset scores under 10
def norm_score():
    global player_score
    global banker_score
    if player_score >= 10:
        player_score -= 10
    if banker_score >= 10:
        banker_score -= 10


norm_score()

# declare winner function
def declare_winner():
    global player_score
    global banker_score

    if player_score == banker_score:
        print("Tie Score!")
    elif player_score > banker_score:
        print("Player Wins!")
    elif player_score < banker_score:
        print("Banker Wins!")

#Banker add function
def banker_add():
    global banker_score
    global card_values
    global game_cards
    print("Banker Hits")
    banker_score += card_values[5]
    norm_score()
    print(game_cards[5])
    print("The Banker's Score is now " + str(banker_score))

#Banker Draw Function
def banker_draw():
    global player_score
    global banker_score
    global card_values

    if card_values[4] == 0 or card_values[4] == 1 or card_values[4] == 9:
        if banker_score > 3:
            print("Banker Stays")
        if banker_score < 4:
            banker_add()

    if card_values[4] == 2 or card_values[4] == 3:
        if banker_score > 4:
            print("Banker Stays")
        if banker_score < 5:
            banker_add()

    if card_values[4] == 4 or card_values[4] == 5:
        if banker_score > 5:
            print("Banker Stays")
        if banker_score < 6:
            banker_add()

    if card_values[4] == 6 or card_values[4] == 7:
        if banker_score > 6:
            print("Banker Stays")
        if banker_score < 7:
            banker_add()

    if card_values[4] == 8:
        if banker_score > 2:
            print("Banker Stays")
        if banker_score < 3:
            banker_add()



#Display
print("Player Cards: " + game_cards[0] + " and " + game_cards[1])
print("The Player's Score is " + str(player_score))
print("            ")

print("Banker Cards: " + game_cards[2] + " and " + game_cards[3])
print("The Banker's Score is " + str(banker_score))
print("            ")

# Game Loop
running = True
while running:

# Check for Natural Winner and Natural Tie
    if player_score == 9 or player_score == 8 or banker_score == 9 or banker_score == 8:
        declare_winner()
        if player_score == 9 and player_score > banker_score:
            print("Natural Win for the Player!")
            break
        elif banker_score == 9 and banker_score > player_score:
            print("Natural Win for the Banker!")
            break
        elif player_score == 8 and player_score > banker_score:
            print("Natural Win for the Player!")
            break
        elif banker_score == 8 and banker_score > player_score:
            print("Natural Win for the Banker!")
            break

# Player Stays
    elif player_score == 6 or player_score == 7:
        print("Player Stays")
        if banker_score == 6 or banker_score == 7:
            print("Banker Stays")
        if banker_score < 6:
            banker_add()
        declare_winner()
        break

# Player Hits
    elif player_score < 6:
        player_score += card_values[4]
        print("Player Hits! ")
        print(game_cards[4])
        norm_score()
        print("The Player's Score is now " + str(player_score))
        banker_draw()
        declare_winner()
        break
