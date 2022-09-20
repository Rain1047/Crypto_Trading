from socket import create_server
from yahooquery import Screener
import yfinance as yf
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# crypto ticker list 
s = Screener()
data = s.get_screeners('all_cryptocurrencies_us', count=250)
# data is in the quotes key
dicts = data['all_cryptocurrencies_us']['quotes']
symbols = [d['symbol'] for d in dicts]
# symbols

Ticker = yf.Ticker("BTC-USD")
Data = Ticker.history(period="max",interval='1d')
# BTC_Data
data_engine = create_engine('sqlite:///dataset/crypto_data.db')
Data.to_sql('BTC', con=data_engine)
