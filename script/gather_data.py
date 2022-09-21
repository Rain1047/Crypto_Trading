from socket import create_server
from yahooquery import Screener
import yfinance as yf
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from tqdm import tqdm

class collector():
    def __init__(self):
        pass
    
    def gather_data(self):
        # 关闭警告
        pd.set_option('mode.chained_assignment', None)
        # crypto ticker list 
        s = Screener()
        data = s.get_screeners('all_cryptocurrencies_us', count=250)
        # data is in the quotes key
        dicts = data['all_cryptocurrencies_us']['quotes']
        symbols = [d['symbol'] for d in dicts]
        # symbols
        symbol_str = ''
        for symbol in symbols:
            symbol_str = symbol_str + symbol + ' '
        # use threads
        data = yf.download(
            tickers = symbol_str, 
            period = '2y', 
            interval = '1d', 
            group_by = 'ticker', 
            threads = True,
        )
        for symbol in tqdm(symbols):
            df = data[symbol]
            df['Datatime'] = df.index
            data_engine = create_engine('sqlite:///dataset/crypto_data.db')
            df.to_sql(symbol, con=data_engine, if_exists='replace',index=None)

col = collector()
col.gather_data()