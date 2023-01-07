#            ------------------------Scopa Card Game------------------------
import random
import time

# my 2 Strategies to test
' - The chance of winning increases if you throw the lowest cards first and keep high cards so you get more sums'
' - If you have the chance of getting golds take them because they could give you a point'

#CREATION OF THE CARD OBJECT
class Card(object):
    def __init__(self, value, seed):
        self.value = value
        self.seed = seed
    
    def show(self):
        print(self.strVal())
        
#Returns a string value of the card properties      
    def strVal(self):
        return str(self.value) + ' ' + self.seed
    
#Returns just the card value    
    def intVal(self):
        return self.value

#Returns just the card seed
    def seedVal(self):
        return self.seed
        
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
            
'''            
    def takingCards(self)
        self.cards.append()
      
        if card is thrown != any sums or cards on the table or table is clear:
            put it with the table cards
        elif card is thrown == card with same value:
                take and put in the points deck
        elif card is thrown == sum:
            if card is thrown = possibleSums:
                let the player pick which sum they want to take
                take and put in the points deck
'''   
#PLAYING CARDS FROM YOUR HAND    
def playCard(self):
    return self.hand.pop()
    
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
    def __init__(self, name, isCpu=False):
        self.isCpu = isCpu
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()
    
'''
#TAKING CARDS WITH SUM OR WITH SAME CARD  (I need first to make the sums and the taking action)



#TAKING CARDS FROM TABLE TO POINTS DECK  
    def takeCard(self):
        return self.cards.append(Card(n, s))    
'''

#MAIN ______________________________________________________________________________________

#DECIDING WHAT GAMEMODE USER WANTS TO PLAY
print('Scopa Card Game!','\n',
    '[1] Single Player','\n',
    '[2] Multi Player','\n',
    '[3] Simulation Game','\n',
    '[4] Rules')
gamemode = int(input('Welcome to my game, select one of the options: '))
while gamemode < 1 or gamemode > 3: #4
    gamemode = int(input('Invalid! Select one of the above options: '))
# time.sleep(0.5)

"""
if gamemode == 1:
    # go to single player mode against bot(CPU)
elif gamemode == 2:
    # go to multiplayer mode
elif gamemode == 3:
    # go to simulation mode
elif gamemode == 4:
    # go to rules
"""
 
#SHUFFLED DECK
deck = Deck()          
deck.shuffle()
'''
# REORDERING THE DECK
deck.build()
deck.show()
'''
#THE 4 STARING CARDS ON THE TABLE
tab = Table()
tab.draw(deck).draw(deck).draw(deck).draw(deck)

#MAKING EACH PLAYER'S HAND BASED ON THE GAMEMODE
players = []
if gamemode == 1:
    player = Player(str(input('What is your name: ')))
    print(player.name +' cards:') 
    print('-------------------')
    player.draw(deck).draw(deck).draw(deck)
    player.showHand()    
    print(' ')
    a = 1
    for card in player.hand:
        print('{}) {}'.format(a, card.strVal()))
        a = a+1
    print(' ')
    players.append(player)
# time.sleep(0.5)

    player = Player('CPU', True)
    print('CPU cards:') 
    print('-------------------')
    player.draw(deck).draw(deck).draw(deck)
    player.showHand()
    print(' ')
    b = 1
    for card in player.hand:
        print('{}) {}'.format(b, card.strVal()))
        b = b+1
    print(' ')
    players.append(player)
# time.sleep(0.5)    

elif gamemode == 2:
    player = Player(str(input('What is your name: ')))
    print(player.name +' cards:') 
    print('-------------------')
    player.draw(deck).draw(deck).draw(deck)
    player.showHand()
    print(' ')
    a = 1
    for card in player.hand:
        print('{}) {}'.format(a, card.strVal()))
        a = a+1
    print(' ')
    players.append(player)
# time.sleep(0.5)

    player = Player(str(input('What is your name: ')))
    print(player.name +' cards:') 
    print('-------------------')
    player.draw(deck).draw(deck).draw(deck)
    player.showHand()  
    print(' ')
    b = 1
    for card in player.hand:
        print('{}) {}'.format(b, card.strVal()))
        b = b+1
    print(' ')
    players.append(player)
# time.sleep(0.5)

elif gamemode == 3:
    player = Player('CPU', True)
    print('CPU 1 cards:') 
    print('-------------------')
    player.draw(deck).draw(deck).draw(deck)
    player.showHand()
    print(' ')
    a = 1
    for card in player.hand:
        print('{}) {}'.format(a, card.strVal()))
        a = a+1
    print(' ')
    players.append(player)
#time.sleep(0.5)    
    player = Player('CPU', True)
    print('CPU 2 cards:') 
    print('-------------------')
    player.draw(deck).draw(deck).draw(deck)
    player.showHand()
    print(' ')
    b = 1
    for card in player.hand:
        print('{}) {}'.format(b, card.strVal()))
        b = b+1
    print(' ')
    players.append(player)
# time.sleep(0.5)
#print(tab.table)

'''
#MAKING EACH PLAYER'S EMPTY POINTS DECK  
pointsDeck1 = PointsDeck()
pointsDeck1.cards.append(player1.playCard() and tab.table)
pointsDeck1.showPdeck()
'''

playing = True

'''
for p in player
    for card in player.hand:
        if Card.value > 0:
            playerTurn = playerTurn + 1
            print('my turn')
'''

#PLAYER 1 AND 2 SCORES
scorePl1 = 0
scorePl2 = 0
'''
#PLAYING LOOP AND NEW TURNS WHEN BOTH PLAYERS FINISHED THEIR CARDS
turn = 1
print('Cards on the table:')
tab.showTable()
print(' ')
while len(deck.cards) > 0 or len(players[0].hand) > 0:
    playing = True
    if len(player1.hand) == 0 and len(player1.hand) == 0 and len(deck.cards) > 0:
        print('New Turn - '+player1.name +' new cards:')
        player1.draw(deck).draw(deck).draw(deck)
        player1.showHand()
        turn = 1
        
#TURN PLAYER 1
    if turn == 1:
        print('Cards on the table:')
        tab.showTable()
        print(' ')
        cardChosen = int(input(player1.name, 'which card do you want to play?'))
        while cardChosen < 1 or cardChosen > len(player1.hand):
            cardChosen = int(input('Invalid! Select one of the cards in your hand: '))
            cardChosen = playCard()
            print(player1.name +' played '+ cardChosen)
            if len(player1.hand) - 1:
                turn = turn + 1
            
            
#TURN PLAYER 2
    elif turn == 2:
        print('Cards on the table:')
        tab.showTable()
        print(' ')
        #cardChosen = int(input(player1.name, 'which card do you want to play?'))
        while cardChosen < 1 or cardChosen > len(player1.hand):
            cardChosen = int(input('Invalid! Select one of the cards in your hand: '))
            if len(player1.hand) - 1:
                turn = turn - 1
                
#END OF THE GAME WHEN DECK RUNS OUT OF CARDS
if len(deck.cards) == 0 and len(player1.hand) == None:
    playing = False
    turn = 0
    print('End game')
'''


# Wording the code so I understand it better
'''
    while deck is not empty and players have cards each:
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
            if card is thrown = possibleSums:
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
        if scorePl1 > scorePl2:
            if gamemode == 3:
                print('The Winner is CPU 1!')
            else:
                print('The Winner is'+ player1.name, '!')
        elif if scorePl1 < scorePl2:
            if gamemode == 1:
                print('The Winner is Player 2 (CPU)!')
            elif  gamemode == 3:
                print('The Winner is CPU 2!')
            else:
                print('The Winner is'+ player2.name, '!')
        elif scorePl1 == scorePl2:
            print('It is a draw!')
 
                        #Graphs
Barcharts of all cards collected, all sums, all points aquired by each player
Pie chart graph for all golden cards collected by each player
Scatter plot graph to record in which turn scopas were taken (grafico a puntini)
Find the mean of all cards taken in each turn and graph with a line graph which turns players took more cards

!I have to calculate all myself without using data packs! NO BUILT IN FUNCTIONS!!!!
'''
