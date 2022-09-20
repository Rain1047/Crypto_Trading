from tvDatafeed import TvDatafeed,Interval
from config import username, password

# initialize tradingview
tv = TvDatafeed(username=username,password=password)

appl = tv.get_hist('AAPL','NASDAQ',)
print(appl)