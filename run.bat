@echo off
color 9
echo [1] BTCINFO [.]
echo [2] ETHINFO [.]
echo [3] BTCGRAPH [.]
echo [4] ETHGRAPH [.]
set /p Choice=Choice:
if "%Choice%" == "1" start python 1.py
if "%Choice%" == "2" start python 2.py
if "%Choice%" == "3" start python 3.py
if "%Choice%" == "4" start python 4.py
