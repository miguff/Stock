import yfinance as yf
import os
import pandas as pd
import plotly.express as px

msft = yf.Ticker("MMM")
history = msft.history(start="2000-01-01", end="2021-07-13")
history.to_csv("History.csv")

df = pd.read_csv('History.csv')

fig = px.line(df, x = 'Date', y = 'Open', title='MMM stock')
fig.show()

"""
Innen kezdődik az effektív kód
"""
payload = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
first_table = payload[0]
second_table = payload[1]
df = first_table
symbols = df['Symbol'].values.tolist()

def dividend_payer():
    stock = []
    for ticker in symbols[:1]:
        Ticker = yf.Ticker(f"{ticker}")
        try:
            if len(Ticker.dividends)/4 > 15:
                stock.append(ticker)
        except:
            pass
    return stock

def reszveny_new_folder(symbol):
    directory = symbol
    parent_dir = "/home/mihalyi/Documents/Programozás/Stocks"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

def reszveny_param(symbol):
    Ticker = yf.Ticker(f"{symbol}")
    Balance_sheet = Ticker.quarterly_balance_sheet
    Financial = Ticker.quarterly_financials
    Cashflow = Ticker.quarterly_cashflow
    Earnings = Ticker.quarterly_earnings
    Balance_sheet.to_csv(f"/home/mihalyi/Documents/Programozás/Stocks/{symbol}/Balance_Sheet.csv")
    Financial.to_csv(f"/home/mihalyi/Documents/Programozás/Stocks/{symbol}/Financials.csv")
    Cashflow.to_csv(f"/home/mihalyi/Documents/Programozás/Stocks/{symbol}/Cashflow.csv")
    Earnings.to_csv(f"/home/mihalyi/Documents/Programozás/Stocks/{symbol}/Earnings.csv")

for ticker in dividend_payer():
    reszveny_new_folder(ticker)
    reszveny_param(ticker)
