from textblob import TextBlob
import pandas as pd

def compute_sentiment(df, ticker):
    df_filtered = df[df['stock'] == ticker].copy()
    df_filtered['sentiment'] = df_filtered['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    daily_sentiment = df_filtered.groupby('date')['sentiment'].mean().reset_index()
    return daily_sentiment