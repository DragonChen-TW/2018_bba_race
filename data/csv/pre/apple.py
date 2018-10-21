#Purpose: pre-processing apple store dataset
import pandas as pd
import numpy as np
from sklearn import datasets

#insert column names incase your csv doesn't have headers
'''column_headers = ["App","Category","Rating", "Reviews", "Size", "Installs", "Type", "Price"
, "Content Rating", "Genres", "Last Updated", "Current Ver", "Android Ver"]
'''
#-----------reading csv------------------------------------
#read csv
df = pd.read_csv('AppleStore.csv')

#-----------processing currency values and drop NaN values--------------------------
#drop those currency values which are not "USD"
#(for the convience of comparing app prices)
df = df[df.currency == "USD"]
df.dropna()

#----------processing columns not needed-------------------
#drop columns not needed
df = df.drop(['cont_rating'], axis=1)

#----------processing columns which should be one hot encoded------
#do one-hot encoding on 'prime_genre' column
prime_genre = pd.get_dummies(df['prime_genre'])
