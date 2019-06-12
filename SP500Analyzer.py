#===============================================================================
# Required for data:
# Data provided by IEX Cloud
# https://iexcloud.io
#===============================================================================

import pandas as pd
# import numpy as np

import configparser

import requests
import json

# loading configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Production Keys and URL
#key=config["DEFAULT"]["KEY"]
#pub_key=config["DEFAULT"]["PUB_KEY"]
#url = config["DEFAULT"]["BASE_URL"]

# Sandbox Keys and URL
key=config["SANDBOX"]["KEY"]
pub_key=config["SANDBOX"]["PUB_KEY"]
url = config["SANDBOX"]["SANDBOX_BASE_URL"]

stocks = pd.read_csv("SP500Data.csv")

# Calculate MACD and RSI for each stock and store to pandas dataframe
# MACD Formula
# 12 day period EMA - 26 day period EMA
# EMA Formula
# (PriceToday * (26/26+1) ) + EMAYesterday(1 - (26/26+1) )
# RSI Formula
# 100 - (100 / 0 + RS)
# Avg Gain = (totalGains/n)
# Avg Loss = (totalLoss/n)
# First RS = (Avg Gain / Avg Loss)
# Smoothed RS ((prev Avg Gain * 13 + Curr Gain) / 14) / ((prev Avg Loss * 13 + Curr Loss) / 14)

for stock in stocks["Symbol"]:
   
    query = url + "/stock/{}/chart/1m?token={}"
    query = query.format(stock, key)
    
    data = requests.get(query)
    
    data = data.json()
    
    df = pd.DataFrame(data)
    
    df = df['close']
    
    df = df.to_frame()
    
    # 26 Day EMA
    exp26 = df.ewm(span = 26, adjust = False).mean()
  
    # 12 Day EMA
    exp12 = df.ewm(span = 12, adjust = False).mean()
  
    macd = exp12 - exp26
  
    # 9 Day EMA Signal Line
    exp9 = macd.ewm(span = 9, adjust = False).mean()
  
    # bullish crossover happens when the MACD crosses above the signal line (Oversold)
    # bearish crossover happens when the MACD crosses below the signal line (Overbought)
    
    # Check the values for the last trading day  
    # Assign a 1 to signify MACD crossed over signal
    if(macd['close'].iloc[-1] > exp9['close'].iloc[-1]):
        stocks.loc[stocks['Symbol'] == stock, 'MACD'] = 1
       
    # Assign a -1 to signify NACD cross below signal line
    elif(macd['close'].iloc[-1] < exp9['close'].iloc[-1]):
        stocks.loc[stocks['Symbol'] == stock, 'MACD'] = -1
          
    # Assign a 0 to signify no cross overs    
    else:
        stocks.loc[stocks['Symbol'] == stock, 'MACD'] = 0
     
    df = pd.DataFrame(data)
    
    df = df['change']
    
    df = df.to_frame()
    
    # Step 1 for RSI
    # Avg Gains and Avg Loss
    pos = 0
    neg = 0

    # Get previous 14 day not 
    prev = df.iloc[-15:-1]

    for index,rows in prev.iterrows():
    
        if(rows['change'] > 0):
            pos += rows['change']
    
        elif(rows['change'] < 0):
            neg += -rows['change']
    
    pos = pos/14
    neg = neg/14

    RS = pos/neg
    
    RSI = 100 - (100/(1+RS))

    # Step 2 Smooth out RS
    # Get current gain or loss
    curr = df.iloc[-1]
    currGain = 0
    currLoss = 0

    if(curr['change'] > 0):
        currGain = curr['change']
        currLoss = 0
    
    else:
        currLoss = -curr['change']
        currGain = 0
    
    
    smooth = (((pos*13)+currGain) / 14) / (((neg*13)+currLoss) /14)
    
    # Less than 30 = Oversold
    # Higher than 70 = Overbought 
    smoothRSI = 100 - (100/(1+smooth))
    
    stocks.loc[stocks['Symbol'] == stock, 'RSI'] = smoothRSI

# Write to CSV
stocks.to_csv("SP500Data.csv", index=False)