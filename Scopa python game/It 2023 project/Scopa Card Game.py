#            ------------------------Scopa Card Game------------------------
import random
import time
import pandas as pd
import re
import os.path as path

# My 2 Strategies to test
' - The chance of winning increases if you throw a card that takes, otherwise throw the smallest card'
' - The chance of winning increases if you take a card that takes, otherwise throw a random card'

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

#BUILD THE DECK OF CARDS 
    def build(self):
        for s in ['Coins', 'Cups', 'Spades', 'Clubs']:
            for n in range(1, 11):
                self.cards.append(Card(n, s))

    def getCardsNum(self):
        return len(self.cards)
    
    def show(self):
        for c in self.cards:
            c.show()
            
#SHUFFLING THE DECK            
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
    def __init__(self, name, isCpu = False, strategy = 3):
        self.isCpu = isCpu
        self.name = name
        self.hand = []
        self.scopaCounter = 0
        self.pointsDeck = []
        self.strategy = strategy

    def reset(self):
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

#COUNTING ALL COINS FROM POINTSDECK
    def getCoinsNum(self):
        coinsNum = 0
        for card in self.pointsDeck:
            if card.isCoin():
                coinsNum += 1  
        return coinsNum

#CHECKING IF PLAYER HAS COLLECTED 7 OF COIN
    def has7Coin(self):
        for card in self.pointsDeck:
            if card.is7Coin():
                return True   
        return False
    
#TESTING STRATEGY 1 FUNCTION  
    def getSmallestCardIndex(self):
        minValue = 11
        minIndex = 0
        count = 1
        for card in self.hand:
            if card.intVal() < minValue:
                minValue = card.intVal()
                minIndex = count
            count += 1
        return minIndex
    
#TESTING STRATEGY 2 FUNCTION     
    def getTakingCardIndex(self):
        count = 1
        comb = tab.getCombinations()
        for card in self.hand:
            if comb[card.intVal() - 1] != None:
                return count
            count += 1
        return -1

#GIVE ALL THE REMAINING CARDS TO LAST PLAYER WHO TOOK FROM TABLE
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
        if self.isCpu == True:
            if self.strategy == 1:   # player throws a card that takes, otherwise the smallest card
                cardChosen = self.getTakingCardIndex()
                if cardChosen < 0:
                    cardChosen = self.getSmallestCardIndex() 
            elif self.strategy == 2: # player throws a card that takes, otherwise random
                cardChosen = self.getTakingCardIndex()
                if cardChosen < 0:
                    cardChosen = random.randint(1, len(self.hand)) 
            else:                    # player throws a random card
                cardChosen = random.randint(1, len(self.hand))
        else:
            cardChosen = input(self.name+' which card do you want to play? ')
            while not cardChosen.isdigit() or not (int(cardChosen) in range(1, len(self.hand) +1)):
                cardChosen = input('Invalid! Select one of the cards in your hand: ')
        playedCard = self.hand.pop(int(cardChosen) - 1)
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

#_______________________________________MAIN _______________________________________

#DECIDING WHAT STRATEGY USER WANTS TO PICK
print('Scopa Card Game!','\n',
    '(1) Strategy 1: The chance of winning increases if you throw a card','\n',
    'that takes or otherwise throw the smallest card in your hand.','\n',
    '(2) Strategy 2: The chance of winning increases if you throw a card','\n',
    'that takes or otherwise throw a random card.','\n',
    '(3) No Strategy to test')
strategyChosen = int(input('Welcome to my game, select one of the options: '))
while strategyChosen < 1 or strategyChosen > 3:
    strategyChosen = int(input('Invalid! Select one of the above options: '))
time.sleep(0.5)

#DECIDING WHAT GAMEMODE USER WANTS TO PLAY
if strategyChosen == 1:
    print('\n',
          'The prediction made from 100 simulations proves that if you follow','\n',
        'the strategy of using a card that takes or otherwise throwing the','\n',
        'smallest card in your hand gives you a chance of winning ','\n',
        'of 71.1% against your opponent.','\n')
    time.sleep(0.5)
    
elif strategyChosen == 2:
    print('\n',
          'The prediction made from 100 simulations proves that if you follow','\n',
        'the strategy of using a card that takes or otherwise throwing a,','\n',
        'random card gives you a chance of winning of 59.9% against your opponent.','\n')
    time.sleep(0.5)
else:
    time.sleep(0.5)

print('Scopa Card Game!','\n',
    '[1] Single Player','\n',
    '[2] Multi Player','\n',
    '[3] Simulation Game','\n',
    '[4] Rules')
gamemode = input('Select one of the options: ')
while not gamemode.isdigit() or not (int(gamemode) in range(1, 5)):
        gamemode = input('Invalid! Select one of the above options: ') 
time.sleep(0.5)
   
#RULES AND GOING BACK TO MENU
if int(gamemode) == 4:
    import Rules
    print('Scopa Card Game!','\n',
    '[1] Single Player','\n',
    '[2] Multi Player','\n',
    '[3] Simulation Game')
    gamemode = input('Select one of the options: ')
    while not gamemode.isdigit() or not (int(gamemode) in range(1, 4)):
            gamemode = input('Invalid! Select one of the above options: ') 
    time.sleep(0.5)

#VERYFYING E-MAIL FUNCTION
regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
def check(email):
    if(re.search(regex,email)):
        return True
    else:
        return False

#MAKING EACH PLAYER BASED ON THE GAMEMODE
players = []
nGames = 1

if int(gamemode) == 1:
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

elif int(gamemode) == 2:
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

elif int(gamemode) == 3:
    nGames = int(input('How many simulations do you want to run? '))
    while nGames < 1:
        nGames = int(input('Invalid! Select at least one simulation to run: '))
        
    player = Player('CPU1', True, strategyChosen)
    players.append(player)
    time.sleep(0.5)
    
    player = Player('CPU2', True)
    players.append(player)
    time.sleep(0.5)

#SEEING THE TABLE VALUES IN THE FIRST ROW
df = pd.DataFrame({
    'Games': [],
    'Cards': [],
    'Coins': [],
    'Scopas': [],
    '7 Of Coin': [],
    'Total Points': [],
    'Player': []
})
L = []

#DECIDING THE NUMBER OF GAMES
for gameIndex in range(0, nGames):
    for player in players:
        player.reset()
    if int(gamemode) == 3:
        print('________________________________NEW SIMULATION GAME________________________________')
        
    #SHUFFLED DECK
    deck = Deck()          
    deck.shuffle()

    #THE 4 STARTING CARDS ON THE TABLE
    tab = Table()
    tab.draw(deck).draw(deck).draw(deck).draw(deck)
    tab.createComb()

    #PLAYING LOOP AND NEW TURNS WHEN BOTH PLAYERS FINISHED THEIR CARDS
    print('\n')

    while len(deck.cards) > 0:
        print('New Turn')
        for player in players:
            player.draw(deck).draw(deck).draw(deck)
            if int(gamemode) == 1 or int(gamemode) == 2:
                time.sleep(0.5)
            else:
                time.sleep(0.1)
        lastTakenIndex = 0
        while players[0].hasCards():
            for player in players:
                tab.showTable()
                if int(gamemode) == 1 or int(gamemode) == 2:
                    time.sleep(0.5)
                else:
                    time.sleep(0.1)
                if player.playCard(tab) == True:
                    lastTakenIndex = players.index(player)
                if int(gamemode) == 1 or int(gamemode) == 2:
                    time.sleep(0.5)
                else:
                    time.sleep(0.1)
    players[lastTakenIndex].takeRemainingCards()
    

#                     #DEBUG CODE
#     
#                     tot = 0
#                     for p in players:
#                         tot += p.getHandCardsNum() + p.getCardsNum()
#                         print("Cards in player's hand" + p.getName() + ": " + str(p.getHandCardsNum()))
#                         print("Cards in Points Deck" + p.getName()+ ": " + str(p.getCardsNum()))
#                     tot += tab.getCardsNum() + deck.getCardsNum()
#                     print("Table Cards: " + str(tab.getCardsNum()))
#                     print("Deck Cards: " + str(deck.getCardsNum()))
#                     print("Total Cards: " + str(tot))
#                     time.sleep(0.1)               

    #PLAYER 1 AND 2 SCORES, CARDS, COINS, SCOPAS AND WHO COLLECTED 7 COIN
    playerScores = [0] * len(players)
    player7CoinNum = [0] * len(players)
    playerCoinsNum = [0] * len(players)
    playerCardsNum = [0] * len(players)
    playerScopaNum = [0] * len(players)

    for playerIndex in range(0, len(players)):
        player = players[playerIndex]
        player7CoinNum[playerIndex] = 1 if player.has7Coin() else 0
        playerScores[playerIndex] = playerScores[playerIndex] + player.getScopaNum()
        playerScores[playerIndex] = playerScores[playerIndex] + player7CoinNum[playerIndex]
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
    
    #PRINTING THE RESULTS OF GAME
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
    
    #NOMINATING A WINNER
    if playerScores[0] > playerScores[1]:
        if int(gamemode) == 3:
            print('The Winner is CPU 1!')
        else:
            print('The Winner is '+ players[0].name+'!')
    elif playerScores[0] < playerScores[1]:
        if int(gamemode) == 1:
            print('The Winner is Player 2 (CPU)!')
        elif  int(gamemode) == 3:
            print('The Winner is CPU 2!')
        else:
            print('The Winner is '+ players[1].name+'!')
    elif playerScores[0] == playerScores[1]:
        print("It's a Draw!")
    print('End game!')
    time.sleep(0.1)
    
#SAVE EACH GAME WITH DATA IN CSV FILE
    #PLAYER 1
    l = []
    l.append(gameIndex+1)
    l.append(playerCardsNum[0])
    l.append(playerCoinsNum[0])
    l.append(playerScopaNum[0])
    l.append(player7CoinNum[0])
    l.append(playerScores[0])
    l.append(players[0].getName())
    L.insert(gameIndex, l)
    #PLAYER 2
    l = []
    l.append(gameIndex+1)
    l.append(playerCardsNum[1])
    l.append(playerCoinsNum[1])
    l.append(playerScopaNum[1])
    l.append(player7CoinNum[1])
    l.append(playerScores[1])
    l.append(players[1].getName())
    L.append(l)
for l in L:
    df = df.append(pd.Series(l, index=df.columns), ignore_index=True)

df.to_csv('ScoreStoreFile.csv', ',', mode='w')


#100 SIMULATIONS I RUN AND SAVED DATA IN EACH CSV FOR EACH STRATEGY USED (GRAPHS ARE IN EACH CSV)
'''
if strategyChosen == 1:
    df.to_csv('Strategy 1 test.csv', ',', mode='w')
elif strategyChosen == 2:
    df.to_csv('Strategy 2 test.csv', ',', mode='w')
'''

#MAKING THE TABLE WITH ALL GAMES RECORDED ACCESSIBLE TO USER THROUGH E-MAIL
if int(gamemode) == 1 or int(gamemode) == 2:
    win = playerScores[0] > playerScores[1]
    draw = playerScores[0] == playerScores[1]
    loss = playerScores[0] < playerScores[1]
    strategy1 = strategyChosen == 1
    strategy2 = strategyChosen == 2
    noStrategy = strategyChosen == 3
    if path.exists('Games Recorded.csv'):
        df = pd.read_csv('Games Recorded.csv', index_col=0 )
    else:
        df = pd.DataFrame({
            'Email': [],
            'Games played': [],
            'Wins': [],
            'Draws': [],
            'Losses': [],
            'Strategy 1': [],
            'Strategy 2': [],
            'No strategy': []
        })

    if len(df.loc[df['Email'] == player1Email]) == 0:
        newRow = {'Email': player1Email,
                   'Games played': 1,
                   'Wins': 1 if win else 0,
                   'Draws': 1 if draw else 0,
                   'Losses': 1 if loss else 0,
                   'Strategy 1': 1 if strategy1 else 0,
                   'Strategy 2': 1 if strategy2 else 0,
                   'No strategy': 1 if noStrategy else 0}
        df = df.append(newRow, ignore_index=True)
    else:
        lIndex = df.index[df['Email'] == player1Email].tolist()
        df.at[lIndex[0],'Games played'] += 1
        if win == True:
            df.at[lIndex[0],'Wins'] += 1
        if draw == True:
            df.at[lIndex[0],'Draws'] += 1
        if loss == True:
            df.at[lIndex[0],'Losses'] += 1
        if strategy1 == True:
            df.at[lIndex[0],'Strategy 1'] += 1
        if strategy2 == True:
            df.at[lIndex[0],'Strategy 2'] += 1
        if noStrategy == True:
            df.at[lIndex[0],'No strategy'] += 1
    df.to_csv('Games Recorded.csv', ',', mode='w')

if int(gamemode) == 2:
    win = playerScores[1] > playerScores[0]
    draw = playerScores[1] == playerScores[0]
    loss = playerScores[1] < playerScores[0]
    strategy1 = strategyChosen == 1
    strategy2 = strategyChosen == 2
    noStrategy = strategyChosen == 3
    if path.exists('Games Recorded.csv'):
        df = pd.read_csv('Games Recorded.csv', index_col=0 )
    else:
        df = pd.DataFrame({
            'Email': [],
            'Games played': [],
            'Wins': [],
            'Draws': [],
            'Losses': [],
            'Strategy 1': [],
            'Strategy 2': [],
            'No strategy': []
        })

    if len(df.loc[df['Email'] == player2Email]) == 0:
        newRow = {'Email': player2Email,
                   'Games played': 1,
                   'Wins': 1 if win else 0,
                   'Draws': 1 if draw else 0,
                   'Losses': 1 if loss else 0,
                   'Strategy 1': 1 if strategy1 else 0,
                   'Strategy 2': 1 if strategy2 else 0,
                   'No strategy': 1 if noStrategy else 0}
        df = df.append(newRow, ignore_index=True)
    else:
        lIndex = df.index[df['Email'] == player2Email].tolist()
        df.at[lIndex[0],'Games played'] += 1
        if win == True:
            df.at[lIndex[0],'Wins'] += 1
        if draw == True:
            df.at[lIndex[0],'Draws'] += 1
        if loss == True:
            df.at[lIndex[0],'Losses'] += 1
        if strategy1 == True:
            df.at[lIndex[0],'Strategy 1'] += 1
        if strategy2 == True:
            df.at[lIndex[0],'Strategy 2'] += 1
        if noStrategy == True:
            df.at[lIndex[0],'No strategy'] += 1
    df.to_csv('Games Recorded.csv', ',', mode='w')

#GRAPHING THE DATA ACQUIRED
import ScoreStore

# Wording the code so I understand it better
'''
while deck is != empty and players have cards each:
    draw 3 cards to the players 
        
#TURNS AND GAMEPLAY
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
        
#POINTS COUNTER      
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
    if gamemode == 3:
        print('The Winner is CPU 2!')
    elif gamemode == 1:
        print('The Winner is Player 2 (CPU)!')
    else:
        print('The Winner is'+ players[1].name+'!')
elif scorePl1 == scorePl2:
    print('Draw!') 
   
END MAIN
