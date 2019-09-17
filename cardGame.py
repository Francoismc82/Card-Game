# To play a hand of Blackjack the following steps must be followed:\n",
    # "1. Create a deck of 52 cards\n",
    # "2. Shuffle the deck\n",
    # "3. Ask the Player for their bet\n",
    # "4. Make sure that the Player's bet does not exceed their available chips\n",
    # "5. Deal two cards to the Dealer and two cards to the Player\n",
    # "6. Show only one of the Dealer's cards, the other remains hidden\n",
    # "7. Show both of the Player's cards\n",
    # "8. Ask the Player if they wish to Hit, and take another card\n",
    # "9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.\n",
    # "10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17\n",
    # "11. Determine the winner and adjust the Player's chips accordingly\n",
    # "12. Ask the Player if they'd like to play again"
 
    
    # "A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without busting. As a starting point in your program, you may want to assign variables to store a list of suits, ranks, and then use a dictionary to map ranks to values."

#Step 1: Import the random module. This will be used to shuffle the deck prior to dealing. Then, declare variables to store suits, ranks and values. This is a common practice used to control the flow of the game.**\n",

import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}


playing = True

#Step 2: Create a Card Class
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

#Step 3: Create a Deck Class

class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\\n '+card.__str__() # add each Card object's print string
            return 'The deck has:' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
 
#Step 4: Create a Hand Class**<br>\n",

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        
    def adjust_for_ace(self):
        self.aces += 1  # add to self.aces
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# We added code to the add_card method to bump self.aces whenever an ace is brought into the hand, and added code to the adjust_for_aces method that decreases the number of aces any time we make an adjustment to stay under 21.

#Step 5: Create a Chips Class
# In addition to decks of cards and hands, we need to keep track of a Player's starting chips, bets, and ongoing winnings. This could be done using global variables, but in the spirit of object oriented programming, let's make a Chips class instead!"

class Chips:
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        

# Step 6: Write a function for taking bets

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break
                
#Step 7: Write a function for taking hits
#Either player can take hits until they bust. This function will be called during gameplay anytime a Player requests a hit, or a Dealer's hand is less than 17. It should take in Deck and Hand objects as arguments, and deal one card off the deck and add it to the Hand. You may want it to check for aces in the event that a player's hand exceeds 21."

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
#Step 8: Write a function prompting the Player to Hit or Stand
 
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break
#Step 9: Write functions to display cards
 
def show_some(player,dealer):
    print("Dealer's Hand: ")
    print(" <card hidden> ")
    print('',dealer.cards[1])
    print("Player's Hand: ", *player.cards, sep='\\n ')

def show_all(player,dealer):
    print("Dealer's Hand: ", *dealer.cards, sep='\\n ')
    print("Dealer's Hand = ",dealer.value)
    print("Player's Hand: ", *player.cards, sep='\\n ')
    print("Player's Hand = ",player.value)

#QUICK NOTES ABOUT PRINT STATEMENTS:
# * The asterisk <code>*</code> symbol is used to print every item in a collection, and the <code>sep='\\n '</code> argument prints each item on a separate line.

#Step 10: Write functions to handle end of game scenarios
 
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
    
print('Welcome to BlackJack! Get as close to 21 as you can without going over!, Dealer hits until she reaches 17. Aces count as 1 or 11.')

# Create & shuffle the deck, deal two cards to each player
deck = Deck()
deck.shuffle
player_hand = Hand()
player_hand.add_card(deck.deal())
player_hand.add_card(deck.deal())
dealer_hand = Hand()
dealer_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())

# Set up the Player's chips
 
player_chips = Chips()  # remember the default value is 100

# Prompt the Player for their bet
 
take_bet(player_chips)

# Show cards (but keep one dealer card hidden)
 
show_some(player_hand,dealer_hand)
while True:  # recall this variable from our hit_or_stand function
    # Prompt for Player to Hit or Stand
    hit_or_stand(deck,player_hand)
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    # If player's hand exceeds 21, run player_busts() and break out of loop
    if player_hand.value > 21:
        player_busts(player_hand,dealer_hand,player_chips)
        break
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    # Show all cards
     
    show_all(player_hand,dealer_hand)
    
    # Run different winning scenarios
    if dealer_hand.value > 21:
        dealer_busts(player_hand,dealer_hand,player_chips)
        
    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_hand,dealer_hand,player_chips)
        
    elif dealer_hand.value < player_hand.value:
        player_wins(player_hand,dealer_hand,player_chips)
        
    else:
        push(player_hand,dealer_hand)
        
    # Inform Player of their chips total
    print("Player's winnings stand at: ",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break