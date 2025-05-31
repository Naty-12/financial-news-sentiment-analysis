# scripts/publisher_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def top_publishers(df: pd.DataFrame, n: int = 10) -> pd.Series:
    """
    Returns the top N publishers by article count.

    Args:
        df (pd.DataFrame): DataFrame containing a 'publisher' column.
        n (int): Number of top publishers to return.

    Returns:
        pd.Series: Top N publishers and their counts.
    """
    return df['publisher'].value_counts().head(n)

class PublisherPlotter:
    def __init__(self, top_publishers: pd.Series):
        self.top_publishers = top_publishers

    def plot_bar(self):
        """
        Plots a bar chart of the top publishers.
        """
        plt.figure(figsize=(10, 6))
        self.top_publishers.plot(kind='bar', color='skyblue')
        plt.title('Top Publishers by Article Count')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()