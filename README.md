# S&P 500 Analyzer

This program analyzes the constituents of the S&P 500 by calculating the MACD and RSI to determine if the stock is in oversold
or overbought conditions. The historical data is from IEX in JSON format. The stock symbol, MACD, and RSI are saved to a CSV file that
is read by an automated trading program using E-Trade's API to determine if the stock should be bought or shorted. 

More features will be added with the next versions, such as adding a database to remove the need for CSV files, complete further analysis
of the stocks, and finally integrating this program with the automated trading program.

# Running the Program

This program requires you to have pandas, requests and json libraries.

If you don't have them, open up command line on Windows and type in pip install *Library Name*. For example, if you don't have requests
just type in pip install requests. 

Next, you'll need an API key from IEX, they have different tiers including a free teir. 
The key can be obtained here: https://iextrading.com/developer/

After you have all the required libraries and an API key, you'll need to edit the config file. Underneath [DEFAULT] you can see KEY = , 
after the equal sign enter your secret key and under PUB_KEY = , you can add your publishable key.

There is a sandbox and production URL, by default this one uses the sandbox environment for testing. To use real data, in the python code change the the variables to be:
key=config["DEFAULT"]["KEY"]
pub_key=config["DEFAULT"]["PUB_KEY"]
url = config["DEFAULT"]["BASE_URL"]

Next download the python file, config file and the SP500Data.csv files and make sure they are all on the same directory.

Now you can run the python program.

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
