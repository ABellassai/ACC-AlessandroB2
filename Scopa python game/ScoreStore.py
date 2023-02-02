import pandas as pd
import csv
import os

#I can make a lisrt of sums for every turn
#Output:
'''
        sums player1  sums player2
  Turn1      420         50
  Turn2      380         40
  Turn3      390         45
'''
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
