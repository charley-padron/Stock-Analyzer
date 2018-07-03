# StockScreener
This project is contains a small GUI and asks a user to input stocks they would like to research, seperated by commas.

The string of stocks then seperated by the commas to search for each one individually and retreive the stock's dates, open, close, high and low prices, as well as the volume and saved in pandas.

This information is used to graph the stocks performan from the dates available; later, the stock's Moving Average Convergence and Divergence (MACD) and Relative Strength Index (RSI) are calculated and graphed on the chart. This will be done for all stocks inputed by the user.

Useful links for the MACD and RSI:

https://www.investopedia.com/terms/r/rsi.asp

https://www.investopedia.com/terms/m/macd.asp

The MACD and RSI are calculated using pandas and it's built-in functions.

Code for this project will be gradually added as features are added and improved.

In order to run this application, you will need to download StockScreener.py and in the variable api_key, you must enter your key from alphavantage.co.

The key is free and all it needs is email address. 

After replacing the empty string (api_key = "") with your key, (api_key = "##########") you can run the program. 
