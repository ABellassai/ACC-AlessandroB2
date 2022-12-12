#Scopa Card Game

import random

#CREATION OF THE DECK
class Card:
    def __init__(self, value, seed):
        self.value = value
        self.seed = seed
        
seeds = ['coins', 'cups', 'spades', 'clubs']
deck = []
for i in range(4):
    for j in range(1, 11):
        deck.append(Card(j, seeds[i]))

for i in deck:
    print(i.seed, i.value) 

def shuffle(deck):
    random.shuffle(deck.cards)
    
def deal(self, )
Player 1 = []
Player 2 = []
class Player:
    hand = None
    flipKey = None
    snapKey = None

    def __init__(self, name, flipKey, snapKey):
        self.hand = []
        self.flipKey = flipKey
        self.snapKey = snapKey
        self.name = name
    
    def draw(self, deck):
        self.hand.append(deck.deal())
    
    def play(self):
        return self.hand.pop(0)
    
    
pl = Player.hand
print(pl)