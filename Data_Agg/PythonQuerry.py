#Aggregating data Using Python Pandas#


#1 Aggregate by zip_code

import pandas as pd
df = pd.read_csv(r'C:\Users\2016-2019.csv')
df_aggr = df.groupby(['zip_code', 'item_description']).bottles_sold.sum()
df_aggr.to_csv(r'C:\Users\item_pop.csv')


#2 Aggregate by store_number and creating a percentage column

import pandas as pd
df = pd.read_csv(r'C:\Users\2016-2019.csv')
item_sum = df.groupby(['store_number', 'item_number', 'item_description']).bottles_sold.sum()
item_sum.to_csv(r'C:\Users\aggragated.csv')

df = pd.read_csv(r'C:\Users\aggragated.csv')
df["Sales_percentage"] = (df["bottles_sold"]/sum(df["bottles_sold"]))*100
df.to_csv(r'C:\Users\aggragated2.csv', index=False)


