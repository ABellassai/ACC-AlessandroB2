import pandas as pd
import plotly.express as px
import plotly
#import os
#import csv

#I can make a list of sums for every turn
#Output:
'''
        sums player1  sums player2
  Turn1      3           1
  Turn2      6           0
  Turn3      1           4
'''
data = {
  "sums player1": [3, 6, 1],
  "sums player2": [1, 0, 4]
}

#----------------------------------------------------

df = pd.read_csv('ScoreStoreFile.csv')

playerCoinsNum = list(df.loc[1])[1:]
players = list(df.columns)[1:]

df2 = pd.read_csv('ScoreStoreFile.csv')

playerCardsNum = list(df2.loc[1])[1:]
players = list(df2.columns)[1:]

df3 = pd.read_csv('ScoreStoreFile.csv')

playerCardsNum = list(df2.loc[0])[1:]
players = list(df2.columns)[1:]


'''
winList = (df.values.tolist())[0]
winChar = (df.values.tolist())[1]
loseList = (df.values.tolist())[2]
looseChar = (df.values.tolist())[3]
turnCounts = (df.values.tolist())[4]
cardsTaken = (df.values.tolist())[5]
pDeckDifference = (df.values.tolist())[6]
coinDifference = (df.values.tolist())[7]
'''

#Coins Pie chart
fig1 = px.pie(values= playerCoinsNum, names= players)
fig1.show()
#Cards Pie chart
fig2 = px.pie(values= playerCardsNum, names= players)
fig2.show()

'''
#Scopas Scatterplot
fig3 = px.scatter(x = turnCounts, y = cardsTaken)
fig3.show()
#Barchart of player points
fig4 = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig4.show()
'''

'''
# Creating Dataset
chars = []
players = ['PLAYER 1', 'PLAYER 2']
dataChar = [0, 0, 0, 0, 0, 0, 0]
for i in range(len(winChar)):
    dataChar[int(winChar[i] - 1)] += 1
dataPlayer = [0, 0]
for i in range(len(winChar)):
    dataPlayer[int(winChar[i] - 1)] += 1
    
#Creating Plot
fig1 = px.pie(values = dataChar, names = chars)
fig2 = px.pie(values = dataPlayer, names = players)
fig3 = px.scatter(x = turnCounts, y = cardsTaken)
#Show.plot
fig1.show()
fig2.show()
fig3.show()
'''
