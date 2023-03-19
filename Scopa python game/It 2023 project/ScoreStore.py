import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly
import os.path as path

df = pd.read_csv('ScoreStoreFile.csv')

# PIE CHARTS
data1 = {
   "values": df['Total Points'].tolist(),
   "labels": df['Player'].tolist(),
   "domain": {"column": 0},
   "hoverinfo":"label+value",
   "hole": .4,
   "type": "pie"
}
data2 = {
   "values": df['Cards'].tolist(),
   "labels": df['Player'].tolist(),
   "domain": {"column": 1},
   "hoverinfo":"label+value",
   "hole": .4,
   "type": "pie"
}
data3 = {
   "values": df['Coins'].tolist(),
   "labels": df['Player'].tolist(),
   "domain": {"column": 2},
   "hoverinfo": "label+value",
   "hole": .4,
   "type": "pie"
}
data = [data1,data2,data3]
layout = go.Layout(
   {
      "title":"Pie Charts",
      "grid": {"rows": 1, "columns": 3},
      "annotations": [
         {
            "font": {
               "size": 20
            },
            "showarrow": False,
            "text": "Total Points",
            "x": 0.11,
            "y": 0.5
         },
         {
            "font": {
               "size": 20
            },
            "showarrow": False,
            "text": "Total Cards",
            "x": 0.5,
            "y": 0.5
         },
         {
            "font": {
               "size": 20
            },
            "showarrow": False,
            "text": "Total Coins",
            "x": 0.89,
            "y": 0.5
         }
      ]
   }
)
fig = go.Figure(data = data, layout = layout)
fig.show()

#BAR CHART
fig = px.bar(df, x='Games', y='Total Points', color='Player', title='Points per game')
fig.show()

#GAMES RECORDED TABLE
if path.exists('Games Recorded.csv'):
    df = pd.read_csv('Games Recorded.csv', index_col=0 )
    fig = go.Figure(layout = go.Layout(title = go.layout.Title(text="Games Recorded")))
    fig.add_trace( 
        go.Table(
            header = dict(values=list(df.columns)),
            cells = dict(values=[df.iloc[:,num] for num in range(len(df.columns))])
        )
    )
    fig.show()
