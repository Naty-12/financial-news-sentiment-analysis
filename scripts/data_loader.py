import pandas as pd
import os

def load_analyst_data(path='../data/raw_analyst_ratings.csv'):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'], format='mixed', utc=True).dt.date
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    return df

def load_stock_data(ticker, base_path='../data/yfinance_data'):
    path = os.path.join(base_path, f"{ticker}_historical_data.csv")
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.sort_values(by='Date', inplace=True)
    df['daily_return'] = df['Close'].pct_change()
    df.rename(columns={'Date': 'date'}, inplace=True)
    return df[['date', 'Close', 'daily_return']]