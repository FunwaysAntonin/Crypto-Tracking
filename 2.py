import pandas_datareader as web
import matplotlib as plt
import mplfinance as mpf
import datetime as dt
import keyboard
import time

print("Loading...")

crypto = 'ETH'
currency = 'EUR'
start = dt.datetime(2022, 1, 1)
end = dt.datetime.now()
dataethinfo = web.DataReader(f'{crypto}-{currency}' ,'yahoo' ,start ,end)
print(dataethinfo)

print("Youc can exit the program")
time.sleep(1000)
