import pandas as pd
import plotly.express as px
import plotly

def pieChart(value1, value2, player1, player2):
    sequence = []
    sequence.append(value1)
    sequence.append(value2)
    players = []
    players.append(player1)
    players.append(player2)
    fig = px.pie(values=sequence, names=players)
    fig.show()
    
def barChart(df):
    fig = px.bar(df, x='Games', y='Total Points', color='Players')
    fig.show()

df = pd.read_csv('ScoreStoreFile.csv')

nGames = int(len(df.loc[0:]) / 2)

totCardsCPU1 = 0
totCardsCPU2 = 0
totCoinsCPU1 = 0
totCoinsCPU2 = 0
totPointsCPU1 = 0
totPointsCPU2 = 0

for gameIndex in range(0, nGames):
    totCardsCPU1 = totCardsCPU1 + df.loc[gameIndex][2]
    totCardsCPU2 = totCardsCPU2 + df.loc[gameIndex + nGames][2]
    totCoinsCPU1 = totCoinsCPU1 + df.loc[gameIndex][3]
    totCoinsCPU2 = totCoinsCPU2 + df.loc[gameIndex + nGames][3]
    totPointsCPU1 = totPointsCPU1 + df.loc[gameIndex][6]
    totPointsCPU2 = totPointsCPU2 + df.loc[gameIndex + nGames][6]

pieChart(round(totCardsCPU1 / nGames, 2), round(totCardsCPU2 / nGames, 2), df.loc[0][7], df.loc[nGames][7])
'''
fig = px.pie(df,  values='Cards', names='Players', title='Average of Cards')
fig.show()
'''
pieChart(round(totCoinsCPU1 / nGames, 2), round(totCoinsCPU2 / nGames, 2), df.loc[0][7], df.loc[nGames][7])
pieChart(round(totPointsCPU1 / nGames, 2), round(totPointsCPU2 / nGames, 2), df.loc[0][7], df.loc[nGames][7])
barChart(df)
