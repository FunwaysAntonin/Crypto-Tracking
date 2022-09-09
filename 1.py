import pandas_datareader as web
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import time

print("Loading...")

crypto = 'BTC'
currency = 'EUR'
start = dt.datetime(2022, 1, 1)
end = dt.datetime.now()
databtcinfo = web.DataReader(f'{crypto}-{currency}' ,'yahoo' ,start ,end)
print(databtcinfo)

print("You can close the program")
time.sleep(1000)
