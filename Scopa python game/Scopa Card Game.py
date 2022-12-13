#Scopa Card Game

import random
import time

#Decicing what Gamemode user wants to play
gamemode = int(input('Welcome to my game, select one of the options:')
if gamemode > 0 and gamemode < 4:
    print('[1] Single Player','\n',
    '[2] Multi Player','\n',
    '[3] Rules'))
else:
    print('press the right key')

#CREATION OF THE DECK
class Card:
    def __init__(self, value, seed):
        self.value = value
        self.seed = seed
        
#MAKING ALL THE CARDS VALUES AND SYMBOLS
seeds = ['coins', 'cups', 'spades', 'clubs']
deck = []
for i in range(4):
    for j in range(1, 11):
        deck.append(Card(j, seeds[i]))

for i in deck:
    print(i.seed, i.value) 

def shuffle(deck):
    random.shuffle(deck.cards)

#MAKING THE PLAYERS
Player1 = []
Player2 = []

def deal(self, ):
    player.append()  
    
class Player:
    hand = None
    playCard = None
    takeCard = None

    def __init__(self, name, playCard, takeCard):
        self.hand = []
        self.playCard = playCard
        self.takeCard = takeCard
        self.name = name
    
    def draw(self, deck):
        self.hand.append(deck.deal())
    
    def play(self):
        return self.hand.pop(0)
    
# pl = Player.hand
# print(pl)
