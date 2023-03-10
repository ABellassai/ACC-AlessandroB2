#            ------------------------Scopa Card Game------------------------
import random
import time
import pandas as pd
import re
#import ScoreStore

# my 2 Strategies to test
' - The chance of winning increases if you throw the lowest cards first and keep high cards so you get more sums'
' - If you have the chance of getting golds take them because they could give you a point'
' - If you leave a scopa with a low table that can be taken in  move you could give a free point and higher chance of loosing'

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

    def getCardsNum(self):
        return len(self.cards)
    
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
    
    def getCardsNum(self):
        return len(self.table)
    
    def addCard(self, card):
        self.table.append(card)
        
    def removeCard(self, index):
        return self.table.pop(index)
    
    def clear(self):
        return self.table.clear()
    
    def isEmpty(self):
        return len(self.table) == 0
    
    #MAKING ALL THE POSSIBLE COMBINATION OF SUMS FROM TABLE
    def createComb(self):
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
    
    def getHandCardsNum(self):
        return len(self.hand)
    
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
    
    def takeRemainingCards(self):
        for card in tab.getCards():
            self.pointsDeck.append(card)
        tab.clear()

#PLAYING CARDS FROM YOUR HAND          
    def playCard(self, tab):
        hasTaken = False
        print('\n' + self.name + "'s cards:")
        a = 1
        for card in self.hand:
            print('{}) {}'.format(a, card.strVal()))
            a = a + 1
        cardChosen = int(input(self.name+' which card do you want to play? '))
        while cardChosen < 1 or cardChosen > len(self.hand):
            cardChosen = int(input('Invalid! Select one of the cards in your hand: '))
        playedCard = self.hand.pop(cardChosen - 1)
        comb = tab.getCombinations()
        if comb[playedCard.intVal() - 1] == None:
            tab.addCard(playedCard)
        #TAKING CARDS FROM TABLE TO POINTS DECK  
        else:
            hasTaken = True
            valComb = comb[playedCard.intVal() - 1].split(',')
            for i in reversed(range(len(valComb))):
                self.pointsDeck.append(tab.removeCard(int(valComb[i])))
            self.pointsDeck.append(playedCard)
            if tab.isEmpty():
                self.scopaCounter += 1
                print(self.name + ' has done a SCOPA!')
                print('The table is now empty')
        tab.createComb()
        print(self.name +' played the '+ playedCard.strVal())
        return hasTaken
        
    #PLAYING CARDS FROM Dummy CPU
    def CPUplayCard(self, tab):
        hasTaken = False
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
            hasTaken = True
            valComb = comb[playedCard.intVal() - 1].split(',')
            for i in reversed(range(len(valComb))):
                self.pointsDeck.append(tab.removeCard(int(valComb[i])))
            self.pointsDeck.append(playedCard)
            if tab.isEmpty():
                self.scopaCounter += 1
                print(self.name + ' has done a SCOPA!')
                print('The table is now empty')
        tab.createComb()
        print(self.name +' played the '+ playedCard.strVal())
        return hasTaken
    
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

#DECIDING WHAT STRATEGY USER WANTS TO PICK
Strat1Prediction = 67
Strat2Prediction = 56

print('Scopa Card Game!','\n',
    '(1) Strategy 1: The chance of winning increases if you throw the lowest','\n',
    'cards first from your hand and keep high cards so you get more sums','\n',
    '(2) Strategy 2: If you collect more coin cards you have','\n',
    'better chance of winning the game','\n',
    '(3) No Strategy to test')
strategyChosen = int(input('Welcome to my game, select one of the options: '))
while strategyChosen < 1 or strategyChosen > 3:
    strategyChosen = int(input('Invalid! Select one of the above options: '))
time.sleep(0.5)

#DECIDING WHAT GAMEMODE USER WANTS TO PLAY
if strategyChosen == 1:
    print('\n',
          'The prediction made from the simulation proves that if you follow','\n',
        'the strategy of using clower cards and saving the higher cards ','\n',
        'to take more sums on the table gives you a chance of winning ','\n',
        'of % against your opponent.','\n')
            #'+ str(Strat1Prediction) + '
    time.sleep(0.5)
    
elif strategyChosen == 2:
    print('\n',
          'The prediction made from the simulation proves that if you follow','\n',
        'the strategy of collecting coins during the game,','\n',
        'gives you a chance of winning of % against your opponent.','\n')
                                        #'+ str(Strat2Prediction) + '
    time.sleep(0.5)
else:
    time.sleep(0.5)
    
print('Scopa Card Game!','\n',
    '[1] Single Player','\n',
    '[2] Multi Player','\n',
    '[3] Simulation Game','\n',
    '[4] Rules')
gamemode = int(input('Welcome to my game, select one of the options: '))
while gamemode < 1 or gamemode > 4:
    gamemode = int(input('Invalid! Select one of the above options: '))
time.sleep(0.5)
 
#SHUFFLED DECK
deck = Deck()          
deck.shuffle()

#THE 4 STARING CARDS ON THE TABLE
tab = Table()
tab.draw(deck).draw(deck).draw(deck).draw(deck)
tab.createComb()
    
#RULES AND GOING BACK TO MENU
if gamemode == 4:
    import Rules
    print('Scopa Card Game!','\n',
    '[1] Single Player','\n',
    '[2] Multi Player','\n',
    '[3] Simulation Game')
    gamemode = int(input('Select one of the options: '))
    while gamemode < 1 or gamemode > 3:
        gamemode = int(input('Invalid! Select one of the above options: '))
#VERYFYING E-MAIL
regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
def check(email):
    if(re.search(regex,email)):
        return True
    else:
        return False
    

#MAKING EACH PLAYER'S HAND BASED ON THE GAMEMODE
players = []

if gamemode == 1:
    player = Player(str(input('Player 1, what is your name: ')))
    players.append(player)
    player1Email = input('Insert a valid E-mail: ')
    check(player1Email) 
    while check(player1Email) == False:
        player1Email = input('Invalid E-mail! Insert an existing Email: ')
    time.sleep(0.5)

    player = Player('CPU', True)
    players.append(player)
    time.sleep(0.5)    

elif gamemode == 2:
    player = Player(str(input('Player 1, what is your name: ')))
    players.append(player)
    player1Email = input('Insert a valid E-mail: ')
    check(player1Email) 
    while check(player1Email) == False:
        player1Email = input('Invalid E-mail! Insert an existing Email: ')
    time.sleep(0.5)

    player = Player(str(input('Player 2, what is your name: ')))
    players.append(player)
    player2Email = input('Insert a valid E-mail: ')
    check(player2Email) 
    while check(player2Email) == False:
        player2Email = input('Invalid E-mail! Insert an existing Email: ')
    time.sleep(0.5)

elif gamemode == 3:
    nSimulation = int(input('How many simulations do you want to run? '))
    while nSimulation < 1:
        nSimulation = int(input('Invalid! Select at least one simulation to run: '))
        
    player = Player('CPU1', True)
    players.append(player)
    time.sleep(0.5)
    
    player = Player('CPU2', True)
    players.append(player)
    time.sleep(0.5)
        
#PLAYING LOOP AND NEW TURNS WHEN BOTH PLAYERS FINISHED THEIR CARDS
print('\n')

while len(deck.cards) > 0:
    print('New Game')
    for player in players:
        player.draw(deck).draw(deck).draw(deck)
        time.sleep(0.1)
    lastTakenIndex = 0
    while players[0].hasCards():
        if gamemode != 3:
            for player in players:
                tab.showTable()
                time.sleep(0.2)
                if player.playCard(tab) == True:
                    lastTakenIndex = players.index(player)
                time.sleep(0.1)
        else:
            for player in players:
                tab.showTable()
                time.sleep(0.2)
                if player.CPUplayCard(tab) == True:
                    lastTakenIndex = players.index(player)
                tot = 0
                
    if gamemode == 3:
        if len(deck.cards) == 0 and nSimulation > 1:
            print('__________________________NEW SIMULATION GAME__________________________')
            deck = Deck() 
            deck.shuffle()
            tab = Table()
            tab.draw(deck).draw(deck).draw(deck).draw(deck)
            tab.createComb()
            for player in players:
                player.pointsDeck = []
            #save simulation data from each game on database
            nSimulation = nSimulation - 1
            
players[lastTakenIndex].takeRemainingCards()

#DEBUG CODE
                
#                 for p in players:
#                     tot += p.getHandCardsNum() + p.getCardsNum()
#                     print("Carte in mano player " + p.getName() + ": " + str(p.getHandCardsNum()))
#                     print("Carte punti player " + p.getName()+ ": " + str(p.getCardsNum()))
#                 tot += tab.getCardsNum() + deck.getCardsNum()
#                 print("Carte table: " + str(tab.getCardsNum()))
#                 print("Carte deck: " + str(deck.getCardsNum()))
#                 print("Carte totali: " + str(tot))
#                 time.sleep(0.1)
                        

#PLAYER 1 AND 2 SCORES CARDS AND COINS COLLECTED (AND 7 COIN)
playerScores = [0] * len(players)
playerCoinsNum = [0] * len(players)
playerCardsNum = [0] * len(players)
playerScopaNum = [0] * len(players)

for playerIndex in range(0, len(players)):
    player = players[playerIndex]
    playerScores[playerIndex] = playerScores[playerIndex] + player.getScopaNum()
    playerScores[playerIndex] = playerScores[playerIndex] + 1 if player.has7Coin() else 0
    playerCoinsNum[playerIndex] = player.getCoinsNum()
    playerCardsNum[playerIndex] = player.getCardsNum()
    playerScopaNum[playerIndex] = player.getScopaNum()

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

print('\n')
for playerIndex in range(0, len(players)):
    print(players[playerIndex].getName() + "'s total Cards are " + str(playerCardsNum[playerIndex]))
    print(players[playerIndex].getName() + "'s total Coins are " + str(playerCoinsNum[playerIndex]))
    if players[playerIndex].has7Coin() == True:
        print(players[playerIndex].getName() + " has the 7 of Coins")
    else:
        print(players[playerIndex].getName() + " hasn't got the 7 of Coins")
    print(players[playerIndex].getName() + "'s total Scopas are " + str(playerScopaNum[playerIndex]))
    print(players[playerIndex].getName() + "'s points: " + str(playerScores[playerIndex]), '\n')

data = {
    "P1":[playerCardsNum[0],playerCoinsNum[0]],
    "P2":[playerCardsNum[1],playerCoinsNum[1]],
    }

df = pd.DataFrame(data, index = ["Cards","Coins"])
df2 = pd.DataFrame()

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

df.to_csv('ScoreStoreFile.csv', ',', mode='w')
df2.to_csv('ScoreStoreFile.csv', ',', mode='w')


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
Calculate frequencies of scopas for each Round. Graph it on histogram histogram
!I have to calculate all myself without using data packs! NO BUILT IN FUNCTIONS!!!!
'''
