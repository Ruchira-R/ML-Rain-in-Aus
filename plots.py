import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
'weatherAUS'

df = pd.read_csv("./dataset/weatherAUS.csv")
'''
num_var = ['MinTemp', 'MaxTemp', 'Temp9am', 'Temp3pm', 'WindGustSpeed', 'WindSpeed3pm', 'Pressure9am', 'Pressure3pm']

plt.figure(figsize=(20,20))

correlation = df.corr()
plt.figure(figsize=(16,12))
plt.title('Correlation Heatmap of Rain in Australia Dataset')
ax = sns.heatmap(correlation, square=True, annot=True, fmt='.2f', linecolor='white')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_yticklabels(ax.get_yticklabels(), rotation=30)           


sns.pairplot(df[num_var], kind='scatter', diag_kind='hist', palette='Rainbow')
plt.show()


categorical= ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow']


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='Reds_r')
plt.show()
'''

rain_data_num = df[['MinTemp','MaxTemp','Rainfall','WindSpeed9am','WindSpeed3pm',
                           'Humidity9am','Humidity3pm','Pressure9am','Pressure3pm',
                           'Temp9am','Temp3pm','RainToday','RainTomorrow']]

mpl.rcParams['patch.force_edgecolor'] = True
ax_list = df.drop(['RainTomorrow'],axis=1).hist(figsize=(20,15),bins=20)
ax_list[2,1].set_xlim((0,100))