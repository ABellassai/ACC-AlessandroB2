#            ------------------------Scopa Card Game------------------------
import random
import time
#import ScoreStore

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
    
    def is7Coin(self):
        return self.value == 7 and self.seed == 'Coins'
    
    def isCoin(self):
        return self.seed == 'Coins'
        
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
    
#MAKING THE TABLE WHERE TO PLAY CARDS
class Table(object):
    def __init__(self):
        self.table = []
        self.combinations = []
    
    def draw(self, deck):
        self.table.append(deck.drawCard())
        return self
    
    def showTable(self):
        print('\n')
        print('This is the table:')
        
        for card in self.table:
            card.show()
        #self.showComb()
    
    def getCards(self):
        return self.table
    
    def addCard(self, card):
        self.table.append(card)
        
    def removeCard(self, index):
        return self.table.pop(index)
    
    def isEmpty(self):
        return len(self.table) == 0
    
    #MAKING ALL THE POSSIBLE COMBINATION OF SUMS FROM TABLE
    def createComb(self):
        counter1 = 1
        counter2 = 1
        combinations = [None] * 10
        for index1 in range(0, len(self.table)):
            card1 = self.table[index1]
            for index2 in range(index1 + 1, len(self.table)):
                card2 = self.table[index2]
                for index3 in range(index2 + 1, len(self.table)):
                    card3 = self.table[index3]
                    for index4 in range(index3 + 1, len(self.table)):
                        card4 = self.table[index4]
                        if card1.intVal() + card2.intVal() + card3.intVal() + card4.intVal() <= 10:
                            combinations[card1.intVal() + card2.intVal() + card3.intVal() + card4.intVal() - 1] = str(index1)+','+str(index2)+','+str(index3)+','+str(index4)
                    if card1.intVal() + card2.intVal() + card3.intVal() <= 10:
                        combinations[card1.intVal() + card2.intVal() + card3.intVal() - 1] = str(index1)+','+str(index2)+','+str(index3)
                if card1.intVal() + card2.intVal() <= 10:
                    combinations[card1.intVal() + card2.intVal() - 1] = str(index1)+','+str(index2)
            combinations[card1.intVal() - 1] = str(index1)
        self.combinations = combinations
        
    def showComb(self):
        for index in range(len(self.combinations)):
            print('{}) {}'.format(index + 1, self.combinations[index]))
            
    def getCombinations(self):
        return self.combinations
            
#MAKING THE PLAYERS
class Player(object):
    def __init__(self, name, isCpu = False):
        self.isCpu = isCpu
        self.name = name
        self.hand = []
        self.scopaCounter = 0
        self.pointsDeck = []

    def getName(self):
        return self.name

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show()
            
#CHECKING IF PLAYER HAS CARDS IN HIS HAND
    def hasCards(self):
        return len(self.hand) > 0
    
    def getScopaNum(self):
        return self.scopaCounter
    
    def getCardsNum(self):
        return len(self.pointsDeck)
    
    def getCoinsNum(self):
        coinsNum = 0
        for card in self.pointsDeck:
            if card.isCoin():
                coinsNum += 1  
        return coinsNum

    def has7Coin(self):
        for card in self.pointsDeck:
            if card.is7Coin():
                return True   
        return False
    
#PLAYING CARDS FROM YOUR HAND          
    def playCard(self, tab):
        print('\n' + self.name + "'s cards:")
        a = 1
        for card in self.hand:
            print('{}) {}'.format(a, card.strVal()))
            a = a + 1
        cardChosen = int(input(self.name+ ' which card do you want to play? '))
        while cardChosen < 1 or cardChosen > len(self.hand):
            cardChosen = int(input('Invalid! Select one of the cards in your hand: '))
        playedCard = self.hand.pop(cardChosen - 1)
        comb = tab.getCombinations()
        if comb[playedCard.intVal() - 1] == None:
            tab.addCard(playedCard)
        #TAKING CARDS FROM TABLE TO POINTS DECK  
        else:
            valComb = comb[playedCard.intVal() - 1].split(',')
            for i in reversed(range(len(valComb))):
                self.pointsDeck.append(tab.removeCard(int(valComb[i])))
                self.pointsDeck.append(playedCard)
            if tab.isEmpty():
                self.scopaCounter += 1
                print(self.name + ' has done a SCOPA! :)')
        tab.createComb()
        print(self.name +' played the '+ playedCard.strVal())
        
        
    def CPUplayCard(self, tab):
        print('\n' + self.name + "'s cards:")
        a = 1
        for card in self.hand:
            print('{}) {}'.format(a, card.strVal()))
            a = a + 1
        cardChosen = random.randint(1, len(self.hand))
        playedCard = self.hand.pop(cardChosen - 1)
        comb = tab.getCombinations()
        if comb[playedCard.intVal() - 1] == None:
            tab.addCard(playedCard)
        #TAKING CARDS FROM TABLE TO POINTS DECK  
        else:
            valComb = comb[playedCard.intVal() - 1].split(',')
            for i in reversed(range(len(valComb))):
                self.pointsDeck.append(tab.removeCard(int(valComb[i])))
                self.pointsDeck.append(playedCard)
            if tab.isEmpty():
                self.scopaCounter += 1
                print(self.name + ' has done a SCOPA! :)')
        tab.createComb()
        print(self.name +' played the '+ playedCard.strVal())
    

#TAKING CARDS WITH SUM OR WITH SAME CARD  (I need first to make the sums and the taking action)
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
    

#MAIN _________________________________________________________________________________________________________________

#DECIDING WHAT GAMEMODE USER WANTS TO PLAY
print('Scopa Card Game!','\n',
    '[1] Single Player','\n',
    '[2] Multi Player','\n',
    '[3] Simulation Game','\n',
    '[4] Rules')
gamemode = int(input('Welcome to my game, select one of the options: '))
while gamemode < 1 or gamemode > 3: #4:
    gamemode = int(input('Invalid! Select one of the above options: '))
time.sleep(0.5)

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

#THE 4 STARING CARDS ON THE TABLE
tab = Table()
tab.draw(deck).draw(deck).draw(deck).draw(deck)
tab.createComb()

#MAKING EACH PLAYER'S HAND BASED ON THE GAMEMODE
players = []

if gamemode == 1:
    player = Player(str(input('Player 1, what is your name: ')))
    players.append(player)
    time.sleep(0.5)

    player = Player('CPU', True)
    players.append(player)
    time.sleep(0.5)    

elif gamemode == 2:
    player = Player(str(input('Player 1, what is your name: ')))
    players.append(player)
    time.sleep(0.5)

    player = Player(str(input('Player 2, what is your name: ')))
    players.append(player)
    time.sleep(0.5)

elif gamemode == 3:
    player = Player('CPU1', True)
    players.append(player)
    time.sleep(0.5)

elif gamemode == 4:
    import Rules
    gamemode = int(input('Welcome to my game, select one of the options: '))
    while gamemode < 1 or gamemode > 3:
        gamemode = int(input('Invalid! Select one of the above options: '))
    time.sleep(0.5)

#PLAYING LOOP AND NEW TURNS WHEN BOTH PLAYERS FINISHED THEIR CARDS
print('\n')
while len(deck.cards) > 0:
    #print('New Turn')
    for player in players:
        player.draw(deck).draw(deck).draw(deck)
    while players[0].hasCards():
        if gamemode == 1:
            for player in players:
                if player == Player.isCPU:
                    tab.showTable()
                    player.playCard(tab)
                else:
                    tab.showTable()
                    player.playCard(tab)
        elif gamemode == 2:
            for player in players:
                tab.showTable()
                player.playCard(tab)
        elif gamemode == 3:
            for player in players:
                tab.showTable()
                time.sleep(0.2)
                player.CPUplayCard(tab)

#PLAYER 1 AND 2 SCORES CARDS AND COINS COLLECTED (AND 7 COIN)
playerScores = [0] * len(players)
playerCoinsNum = [0] * len(players)
playerCardsNum = [0] * len(players)

for playerIndex in range(0, len(players)):
    player = players[playerIndex]
    playerScores[playerIndex] = playerScores[playerIndex] + player.getScopaNum()
    playerScores[playerIndex] = playerScores[playerIndex] + 1 if player.has7Coin() else 0
    playerCoinsNum[playerIndex] = player.getCoinsNum()
    playerCardsNum[playerIndex] = player.getCardsNum()

maxCards = 0
maxCoins = 0
maxIndexCards = -1
maxIndexCoins = -1
for playerIndex in range(0, len(players)):
    if playerCardsNum[playerIndex] > maxCards:
        maxCards = playerCardsNum[playerIndex]
        maxIndexCards = playerIndex
    elif playerCardsNum[playerIndex] == maxCards:
        maxIndexCards = -1
    if playerCoinsNum[playerIndex] > maxCoins:
        maxCoins = playerCoinsNum[playerIndex]
        maxIndexCoins = playerIndex
    elif playerCoinsNum[playerIndex] == maxCoins:
        maxIndexCoins = -1
if maxIndexCards > -1:
    playerScores[maxIndexCards] = playerScores[maxIndexCards] + 1
if maxIndexCoins > -1:
    playerScores[maxIndexCoins] = playerScores[maxIndexCoins] + 1

print('-----------------------------')
for playerIndex in range(0, len(players)):
    print(players[playerIndex].getName() + "'s total cards are " + str(playerCardsNum[playerIndex]))
    print(players[playerIndex].getName() + "'s total Coins are " + str(playerCoinsNum[playerIndex]))
    print(players[playerIndex].getName() + "'s total Scopas are " + str([playerIndex]))
    print(players[playerIndex].getName() + "'s points: " + str(playerScores[playerIndex]), '\n')
if playerScores[0] > playerScores[1]:
    if gamemode == 3:
        print('The Winner is CPU 1!')
    else:
        print('The Winner is '+ players[0].name+'!')
elif playerScores[0] < playerScores[1]:
    if gamemode == 1:
        print('The Winner is Player 2 (CPU)!')
    elif  gamemode == 3:
        print('The Winner is CPU 2!')
    else:
        print('The Winner is '+ players[1].name+'!')
elif playerScores[0] == playerScores[1]:
    print("It's a Draw!")
print('End game :)')

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
        
 #CONTAPUNTI       
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
                print('The Winner is'+ players[0].name+'!')
        elif scorePl1 < scorePl2:
            if gamemode == 1:
                print('The Winner is Player 2 (CPU)!')
            elif  gamemode == 3:
                print('The Winner is CPU 2!')
            else:
                print('The Winner is'+ players[1].name+'!')
        elif scorePl1 == scorePl2:
            print('Draw!')
                        #Graphs
Barcharts of all cards collected, all sums, all points aquired by each player
Pie chart graph for all golden cards collected by each player
Scatter plot graph to record in which turn scopas were taken (grafico a puntini)
Find the mean of all cards taken in each turn and graph with a line graph which turns players took more cards
!I have to calculate all myself without using data packs! NO BUILT IN FUNCTIONS!!!!
''' 
