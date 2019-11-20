import pandas as pd
from pandas import DataFrame
import numpy as np


def normalizer( df, numberOfRows ,colName,mean, sd ):
    for i in range(numberOfRows):
        print(i)
        df[colName][i] = ( df[colName][i] - mean ) / (sd)
    return df

columnsCat = ["Date","Location"	,"WindGustDir","RainToday","RainTomorrow","WindDir9am","WindDir3pm" ]
columnsNum = ["MinTemp", "MaxTemp","Rainfall","Evaporation","Sunshine","WindGustSpeed","WindSpeed9am","WindSpeed3pm","Humidity9am","Humidity3pm","Pressure9am","Pressure3pm","Cloud9am","Cloud3pm","Temp9am","Temp3pm","RISK_MM"]
df = pd.read_csv('./dataset/cleaned.csv')
#print(df)



for i in range(len(columnsNum)):
    print("normalising " + str(columnsNum[i] ))
    df = normalizer(df , len(df[columnsNum[i]]), columnsNum[i], df[columnsNum[i] ].mean() , df[columnsNum[i]].std())

print(df)
df.to_csv("./dataset/normalised.csv")







