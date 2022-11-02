import numpy as np 
import pandas as pd 
# Used to grab the stock prices, with yahoo 
import pandas_datareader as web 
from datetime import datetime 
# To visualize the results 
import matplotlib.pyplot as plt 
import seaborn

stock1 = 'AAPL'
stock2 ='F'
stock3 ='TWTR'
stock4 ='FB'
stock5 ='AAL'
stock6 ='AMZN'
stock7 ='GOOGL'
stock8 ='GE'
stock9 ='TSLA'
stock10 ='IBM'
stock11 ='PYPL'
stock12 ='MSFT'
stock13 ='QQQ'
start = datetime(2017, 1, 1)
symbols_list = [stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10, stock11,stock12,stock13]
#array to store prices
symbols=[]

#array to store prices
symbols=[]
for ticker in symbols_list:     
    r = web.DataReader(ticker, 'yahoo', start)   
    # add a symbol column   
    r['Symbol'] = ticker    
    symbols.append(r)
#concatenate into df
df = pd.concat(symbols)
df = df.reset_index()
df = df[['Date', 'Close', 'Symbol']]
#df.head()
df_pivot=df.pivot('Date','Symbol','Close').reset_index()
df_pivot.head()

corr_df = df_pivot.corr(method='pearson')
#reset symbol as index (rather than 0-X)
corr_df.head().reset_index()
#del corr_df.index.name
corr_df.head(10)

plt.figure(figsize=(13, 8))
seaborn.heatmap(corr_df, annot=True, cmap=None)
plt.figure()
