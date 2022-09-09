import pandas_datareader as web
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
from colorama import *
import keyboard

print("Loading...")

crypto = 'ETH'
currency = 'EUR'
start = dt.datetime(2022, 1, 1)
end = dt.datetime.now()
dataethgraph = web.DataReader(f'{crypto}-{currency}' ,'yahoo' ,start ,end)
mpf.plot(dataethgraph, type='candle', style='yahoo')
