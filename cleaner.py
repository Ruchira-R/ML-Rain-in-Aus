import pandas as pd
from pandas import DataFrame
import numpy as np
import os.path

def cleanCat( df,colName,numberOfRows ):
    for i in range( numberOfRows ):
        if pd.isna(df[colName][i]) :
            try:
                df[colName][i] = df[colName][i-1]
            except:
                for j in df[colName][i:]:
                    if( pd.isna(j) ):
                        pass
                    else:
                        df[colName][i] = j
                        break

    
    return df

def cleanNum( df,colName, numberOfRows ):
    avg =  np.sum(df[colName])  / numberOfRows
    for i in range( numberOfRows ):
        if pd.isna(df[colName][i]) :
            df[colName][i] = avg
    
    return df


columnsCat = ["Date","Location"	,"WindGustDir","RainToday","RainTomorrow","WindDir9am","WindDir3pm" ]
columnsNum = ["MinTemp", "MaxTemp","Rainfall","Evaporation","Sunshine","WindGustSpeed","WindSpeed9am","WindSpeed3pm","Humidity9am","Humidity3pm","Pressure9am","Pressure3pm","Cloud9am","Cloud3pm","Temp9am","Temp3pm","RISK_MM"]
df = pd.read_csv('./dataset/weatherAUS.csv')

print( df )
for i in range(len(columnsCat)):
    print("cleaning " + str(columnsCat[i] ))
    df = cleanCat(df , columnsCat[i], len(df[columnsCat[i]]) )

for i in range(len(columnsNum)):
    print("cleaning " + str(columnsNum[i] ))
    df = df = cleanNum(df , columnsNum[i], len(df[columnsNum[i]]) )

df.to_csv("./dataset/cleaned.csv")
