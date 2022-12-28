#Scopa Card Game

import random
import time
# my 2 Strategies to test
' - The chance of winning increases if you throw the lowest cards first and keep high cards so you get more sums'
' - If you have the chance of getting golds take them because they could give you a point'

#DECIDING WHAT GAMEMODE USER WANTS TO PLAY

print('Scopa Card Game!','\n',
    '[1] Single Player','\n',
    '[2] Multi Player','\n',
    '[3] Rules')
gamemode = int(input('Welcome to my game, select one of the options: '))
while gamemode < 1 or gamemode > 2:
    gamemode = int(input('Invalid! Select one of the above options: '))
# time stop(2)
'''
"""
if gamemode == 1:
    # go to single player mode against bot
elif gamemode == 2:
    # go to multiplayer mode
elif gamemode == 3:
    # go to rules
"""
'''
#CREATION OF THE CARD OBJECT
class Card(object):
    def __init__(self, value, seed):
        self.value = value
        self.seed = seed
    
    def show(self):
        print(self.value, self.seed)
        
#CREATION OF THE SHUFFLED DECK WITH VALUES AND SYMBOLS        
class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s in ['Coins', 'Cups', 'Spades', 'Clubs']:
            for n in range(1, 11):
                self.cards.append(Card(n, s))

    def show(self):
        for c in self.cards:
            c.show()
            
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i],
            
#DRAWING CARDS FROM THE DECK AND SUBTRACTING CARDS FROM THE DECK  
    def drawCard(self):
        return self.cards.pop()
    
#MAKING THE POINTS DECK
class PointsDeck(object):
    def __init__(self):
        self.cards = []
        
    def showPdeck(self):
        for c in self.cards:
            c.show()

#MAKING THE TABLE WHERE TO PLAY CARDS
class Table(object):
    def __init__(self):
        self.table = []
    
    def draw(self, deck):
        self.table.append(deck.drawCard())
        return self
    
    def showTable(self):
        for card in self.table:
            card.show()

#MAKING THE PLAYERS
class Player(object):
    def __init__(self, name):
        self.name = str(input('What is your name: '))
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()
            
#PLAYING CARDS FROM YOUR HAND    
    def playCard(self):
        return self.hand.pop()
 
#SHUFFLED DECK
deck = Deck()          
deck.shuffle()
deck.show()
print('\n')
'''
# REORDERING THE DECK
deck.build()
deck.show()
'''
#THE 4 STARING CARDS ON THE TABLE
table = Table()
table.draw(deck).draw(deck).draw(deck).draw(deck)
table.showTable()
print('\n')

#MAKING EACH PLAYER'S HAND
for p in range(gamemode):
    player1 = Player('A')
    print(player1.name +' cards :')
    player1.draw(deck).draw(deck).draw(deck)
    player1.showHand()
    pointsDeck1 = PointsDeck()
    pointsDeck1.cards.append(player1.hand)
#   pointsDeck1.showPdeck()                 donno how to solve this (help)
    
playerTurn = 0
# playing = True

# for i in range (0,2):
#     for p in Player:
'''
for p in player1.name:
    for card in  > 0:
        playerTurn = playerTurn + 1
        print('my turn')
  '''     
# while playing == True:
 
#     def canPlay(playCard)
'''
I need first to make the sums and the taking action
#TAKING CARDS WITH SUM OR WITH SAME CARD



#TAKING CARDS FROM TABLE TO POINTS DECK  
    def takeCard(self):
        return self.cards.append(Card(n, s))    
'''

'''
    while deck is not empty and players have 3 cards each:
        draw 3 cards to the players 
        
    #turns and gameplay
    
    while 2 players still have cards in their hands:
        if player one hand - 1 card:
            turn of player 2
        if card is thrown != any sums or cards on the table or table is clear:
            put it with the table cards
        elif card is thrown == card with same value:
                take and put in the points deck
        elif card is thrown == sum:
            if card is thrown = more than one sum:
                let the player pick which sum they want to take
                take and put in the points deck
        if card is thrown and table is cleared:
            give one point to player
            print('Scopa!')
            next player plays a card and it is appended to the table
           
    if deck is empty:
        turn = 0
        let the last person who took the cards take all cards from the table
        print('End game')
        pointsDeck1.count(all cards, all coin cards, all scopas)
        pointsDeck2.count(all cards, all coin cards, all scopas)
        
        scorePl1 = 0
        scorePl2 = 0
        
        if pointsDeck1.count(all cards) > pointsDeck2.count(all cards):
            scorePl1 + 1
        elif pointsDeck1.count(all cards) < pointsDeck2.count(all cards):
            scorePl2 + 1
        if pointsDeck1.count(all coin cards) > pointsDeck2.count(all coin cards):
            scorePl1 + 1
        elif pointsDeck1.count(all coin cards) < pointsDeck2.count(all coin cards):
            scorePl2 + 1
        for s in pointsDeck1:                #s stands for scopa
            scorePl1 + 1
        for s in pointsDeck2:
            scorePl2 + 1
            
        print('total score for Player 1: ', scorePl1)
        print('total score for Player 2: ', scorePl2)
        if scorePl1 > scorePl2 :
            print('Winner is Player 1!')
        elif if scorePl1 < scorePl2 :
            print('Winner is Player 2!')
        if scorePl1 == scorePl2 :
            print('It's a draw!')
'''
