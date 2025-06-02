import pandas as pd
import matplotlib.pyplot as plt

def merge_data(daily_sentiment, stock_data):
    merged_df = pd.merge(daily_sentiment, stock_data, on='date', how='inner')
    merged_df.dropna(inplace=True)
    return merged_df

def compute_correlation(merged_df):
    return merged_df['sentiment'].corr(merged_df['daily_return'])

def plot_correlation(merged_df, ticker):
    plt.figure(figsize=(8, 6))
    plt.scatter(merged_df['sentiment'], merged_df['daily_return'], alpha=0.6)
    plt.title(f"{ticker}: Sentiment vs Daily Return")
    plt.xlabel("Average Daily Sentiment")
    plt.ylabel("Daily Stock Return")
    plt.axhline(0, color='gray', linestyle='--')
    plt.axvline(0, color='gray', linestyle='--')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
