import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tmp = pd.read_csv('C:\\Users\\18Abellassai.acc\\Downloads\\popIreland_1999_2019_TrainingData.csv')
tmp = tmp.dropna(axis = 0)
popL = tmp['Population']
yearL = tmp['Year']
plt.scatter(yearL, popL)

m,c = np.polyfit(yearL, popL, 1)

yLine = []
for x in yearL:
    yLine.append(m*x+c)
print('The equation of the model is y= '+str(round(m,2))+'x'+str(round(c,2)))
plt.plot(yearL, yLine)

guessL = []
for year in range(2020, 2023):
    pop = m*year+c
    guessL.append(pop)
    print('The estimate for year',year,'is', round(pop,2))
    
guessYL = [2020, 2021, 2022]
plt.scatter(guessYL, guessL)
plt.show()

def getRealError(est, act):
    error = est - act
    percentage_error = (error/act) * 100
    return percentage_error

actualL = [4977400, 5011500, 5123536]
print('year \t Estimate pop \t Actual pop \t %Error')
for i in range(3):
    print(guessYL[i], '\t', round(guessL[i]), '\t', round(actualL[i]), '\t', round(getRealError(guessL[i], round(actualL[i])), 2))
