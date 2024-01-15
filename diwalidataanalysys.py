# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
import matplotlib as mp
import seaborn as sns
# import csv file
df = pd.read_csv('Diwali_Sales_Data.csv', encoding= 'unicode_escape')
print(df.shape)
df.head()
df.info()
#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
df.info()
#check for null values
pd.isnull(df).sum()
# drop null values
df.dropna(inplace=True)
# change data type
df['Amount'] = df['Amount'].astype('int')
df['Amount'].dtypes

#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})
df.describe()
# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()
gender_amount_mean = df.groupby('Gender')['Amount'].sum()

# Plot the bar graph
plt.figure(figsize=(10, 6))
gender_amount_mean.plot(kind='bar', color=['blue', 'pink'])
plt.title('Average Amount by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Amount')
plt.show()
'''
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sales_gen.plot(kind='bar', figsize=(12, 6), color='coral')
plt.xlabel('Gender')
plt.ylabel('Amount')
plt.show()
'''
