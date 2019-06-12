# S&P 500 Analyzer

This program analyzes the constituents of the S&P 500 by calculating the MACD and RSI to determine if the stock is in oversold
or overbought conditions. The historical data is from IEX in JSON format. The stock symbol, MACD, and RSI are saved to a CSV file that
is read by an automated trading program using E-Trade's API to determine if the stock should be bought or shorted. 

More features will be added with the next versions, such as adding a database to remove the need for CSV files, complete further analysis
of the stocks, and finally integrating this program with the automated trading program.

This is the second version of this project. Previosly, I had used alpha vantage to get the historical data of stocks listed under
the S&P 500 index. Alpha vantage had the disadvantage of only allowing 5 calls per minute which would cause the program to take
100 minutes to get the historical data for the constituents of the S&P 500. 

I then experimented with QUANDL, but they stopped providing new data since 3/27/2018. QUANDL was better for allowing 300 calls 
every 10 seconds making the program quicker.

This new version utilizes IEX for the data. It has better limits than QUANDL at 100 requests per second and also contains current
stock prices and many other feautures. This allows the program to get the prices for the constituents by 5 seconds.

### API Requirement: Data provided by IEX Cloud
https://iexcloud.io

## Useful Links:
https://www.investopedia.com/terms/r/rsi.asp

https://www.investopedia.com/terms/m/macd.asp

http://cns.bu.edu/~gsc/CN710/fincast/Technical%20_indicators/Relative%20Strength%20Index%20(RSI).htm
