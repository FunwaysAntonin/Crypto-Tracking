import pandas_datareader as web
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import keyboard

print("Loading...")

crypto = 'BTC'
currency = 'EUR'
start = dt.datetime(2022, 1, 1)
end = dt.datetime.now()
databtcgraph = web.DataReader(f'{crypto}-{currency}' ,'yahoo' ,start ,end)
mpf.plot(databtcgraph, type='candle', style='yahoo')
