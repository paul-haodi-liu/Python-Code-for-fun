# A text-based BlackJack game. One player versus an automated dealer.
# The player can stand or hit and is able to pick their betting
# amount. The program keeps track of the player's total money and alerts the
# player of wins, losses or busts.

import random

hash_map = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, \
               'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

class Card:
    
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
    def getval(self):
        
        return hash_map[self.rank]
    
class Deck:
    
    def __init__(self):
        
        self.dk = []
        for i in ranks:
            for j in suits:
                card = Card(j,i)
                self.dk.append(card)
       
    def __str__(self):
        
        ha = []
        for cd in self.dk:
            ha.append(cd.rank + ' of ' + cd.suit)
        return '[' + ', '.join(ha) + ']'

    def shuffle(self):
        
        random.shuffle(self.dk)
    

class Hand:
    
    def __init__(self):
        
        self.hd = []
        self.sum = 0
        
    def __str__(self):
        
        ha = []
        for cd in self.hd:
            ha.append(cd.rank + ' of ' + cd.suit)
        return '\n'.join(ha) 
    
    
    def hit(self, card):
        self.hd.append(card)
    
    def sum_cal(self):
        
        self.sum = 0
        tmp = self.hd[:]
        l = len(self.hd)
        aces = []
        
        for i in range(l):

            if tmp[0].rank == 'Ace':
                aces.append(tmp[0])
                tmp.pop(0)

            else:
                self.sum += hash_map[tmp[0].rank]
                tmp.pop(0)
        
        for a in aces:

            if self.sum + 11 <= 21:
                self.sum += 11

            else:
                self.sum += 1
       

class Bankroll:
    
    def __init__(self, balance):
        self.balance = balance
    
    def win(self, amt):
        print('You have won this turn!')
        self.balance += amt
        
    def lose(self, amt):
        print('You have lost this turn!')
        self.balance -= amt
     
    def get_balance(self):
        return self.balance

def replay():

    while True:
        answer = input("Do you want to play again? Enter Yes or No ")
    
        if answer == 'Yes':
            return True
        elif answer == 'No':
            return False
        else:
            pass

def if_hit():
    
    while True:
        answer = input('Do you want to stand of hit? Enter s or h ')
        
        if answer == 's':
            return False
        
        elif answer == 'h':
            return True
        else:
            pass
        
while True:
    
    print('Welcome to the BlackJack Game!')
    # Player places a bet
    bk_roll = Bankroll(100)
    print('You now have a balance of 100.')
    while True:
        try:
            bet = int(input('How many chips would you like to bet? '))
            
        except:
            print('Please input an integer')
            continue
        
        else:
            if bet > 100:
                print('You bet can not be larger than 100')
                continue
            
            else:
                break
    
    # Let's create a deck
    d = Deck()
    d.shuffle()
    # Dealer starts with 1 card face up and 1 card face Down (last one to be checked)
    dealer_hand = Hand()
    dealer_hand.hit(d.dk.pop())
    hidden = d.dk.pop()
    dealer_hand.sum_cal()
    print('\n')
    print("Dealer's hand: ")
    print(dealer_hand)
    print('hidden_card')
    print('\n')
    # Player starts with 2 cards face up
    player_hand = Hand()
    player_hand.hit(d.dk.pop())
    player_hand.hit(d.dk.pop())
    player_hand.sum_cal()
    print("Player's hand: ")
    print(player_hand)
    print('\n')
    
    player_busted = False
    # Player's turn (Hit or Stay)
    while player_hand.sum <= 21:
        
        if if_hit():
            # Receive one more card
            player_hand.hit(d.dk.pop())
            player_hand.sum_cal()
            # Print hands
            print('\n')
            print("Dealer's hand: ")
            print(dealer_hand)
            print('hidden_card')
            print('\n')
            print("Player's hand: ")
            print(player_hand)
            print('\n')
                
        else:
            print('Player stands. Dealer starts to play.')
            break
                
    else:
        print('You are busted!')
        bk_roll.lose(bet)
        print("\nThe player's winning is now", bk_roll.get_balance())
        player_busted = True
            
    if not player_busted:
        # Dealer's turn (If the Player didn't bust)
        dealer_hand.hit(hidden)
        dealer_hand.sum_cal()
        while dealer_hand.sum <= 21:
            # Dealer then hits until they either beat the player or bust
            if dealer_hand.sum > player_hand.sum:
                # Print hands
                print('\n')
                print("Dealer's hand: ")
                print(dealer_hand)
                print("Dealer's point:", dealer_hand.sum)
                print('\n')
                print("Player's hand: ")
                print(player_hand)
                print("Player's point:", player_hand.sum)
                print('\n')
                print('Dealer wins!')
                bk_roll.lose(bet)
                print("\nThe player's winning is now", bk_roll.get_balance())
                break
                
            else:
                dealer_hand.hit(d.dk.pop())
                dealer_hand.sum_cal()
        else:
            print('\n')
            print("Dealer's hand: ")
            print(dealer_hand)
            print("Dealer's point:", dealer_hand.sum)
            print('\n')
            print("Player's hand: ")
            print(player_hand)
            print("Player's point:", player_hand.sum)
            print('\n')
            print('Dealer busts and Player wins!')
            bk_roll.win(bet)
            print("\nThe player's winning is now", bk_roll.get_balance())
    
    # Ask for replay
    if replay():
        continue
    
    else:
        break

