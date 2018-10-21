#Purpose: pre-processing google play store dataset
import pandas as pd
import numpy as np
from sklearn import datasets

#insert column names incase your csv doesn't have headers
'''column_headers = ["App","Category","Rating", "Reviews", "Size", "Installs", "Type", "Price"
, "Content Rating", "Genres", "Last Updated", "Current Ver", "Android Ver"]
'''
#-----------reading csv------------------------------------
#read csv
df = pd.read_csv('googleplaystore.csv')

#-----------processing NaN values--------------------------
#replace value 'Varies with devices ' with NaN and drop na
df = df.replace("Varies with devices", np.NaN)
df.dropna()

#----------processing columns not needed-------------------
#drop columns not needed
df = df.drop(['Type', 'Last Updated', 'Content Rating'], axis=1)

#----------processing columns which should be one hot encoded------
#do one-hot encoding on 'Category' column
cate = pd.get_dummies(df['Category'])
installs = pd.get_dummies(df['Installs'])

#----------processing Size column value--------------------
#replace K/M/G with numbers
for index, row in df.iterrows():
	if("K" in row["Size"] or "k" in row["Size"]):
		row["Size"] = int((float(row["Size"][:-1]))*1000)
	elif("M" in row["Size"] or "m" in row["Size"]):
		row["Size"] = int((float(row["Size"][:-1]))*1000000)
	elif("G" in row["Size"] or "g" in row["Size"]):
		row["Size"] = int((float(row["Size"][:-1]))*1000000000)

	if(str("and up") in str(row["Android Ver"])):
		row["Android Ver"] = row["Android Ver"].replace(" and up","")
		print(row["Android Ver"]);