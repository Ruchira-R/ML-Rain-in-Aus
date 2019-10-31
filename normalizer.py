import pandas as pd
from pandas import DataFrame
import numpy as np

def normalizer( df,colName, numberOfRows ):
    df[colName] = ( df[colName] - df[colName].min() ) / ( df[colName].max() - df[colName].min() )
    return df

columnsCat = ["Date","Location"	,"WindGustDir","RainToday","RainTomorrow","WindDir9am","WindDir3pm" ]
columnsNum = ["MinTemp", "MaxTemp","Rainfall","Evaporation","Sunshine","WindGustSpeed","WindSpeed9am","WindSpeed3pm","Humidity9am","Humidity3pm","Pressure9am","Pressure3pm","Cloud9am","Cloud3pm","Temp9am","Temp3pm","RISK_MM"]
df = pd.read_csv('./dataset/cleaned.csv')
#print(df)



for i in range(len(columnsNum)):
    print("normalising " + str(columnsNum[i] ))
    df = normalizer(df , columnsNum[i], len(df[columnsNum[i]]) )

print(df)
df.to_csv("./dataset/normalised.csv")

