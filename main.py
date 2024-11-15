import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def load_and_clean_data():

# loading gold price and perform initial cleaning

    df = pd.read_csv('Gold  Prices.csv')

    # convert date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # set date as index
    df.set_index('Date', inplace=True)

    # remove any duplicate dates
    df = df[~df.index.duplicated(keep='first')]

    # return cleaned df
    return df

def calculate_price_metrics(df):

# calculate various price metrics

    # calculate daily price change
    df['Daily_Return'] = df['Close'].pct_change()

    # calculate moving averages
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()

    # calculate volatility
    df['Volatility'] = df['Daily_Return'].rolling(window=20).std()

    return df

def plot_price_history(df):

    # creating a plot of gold price history with moving averages
    plt.figure(figsize=(15, 7))
    plt.plot(df.index, df['Close'], label='Close Price', alpha=0.8)
    plt.plot(df.index, df['MA20'], label='20-day MA', alpha=0.7)
    plt.plot(df.index, df['MA50'], label='50-DAY MA', alpha=0.7)

    plt.title('Gold price history with moving averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('gold_price_history.png')
    plt.close()

def main():
    print('Loading and cleaning data...')
    df = load_and_clean_data()

    # calculate metrics
    df = calculate_price_metrics(df)

    # generate summary statistics
    print("\nSummary Statistics:")
    print(df[['Open', 'High', 'Low', 'Close', 'Volume']].describe())

    # plot price history
    print("\nCreating price history plot:")
    plot_price_history(df)

    # calculate and display some basic analytics
    print("\nBasic Analytics:")
    print(f"Average Daily Return: {df['Daily_Return'].mean():.4}")
    print(f"Daily Return Volatility: {df['Daily_Return'].std():.4}")
    print(f"Highest Closing Price: {df['Close'].max():.2f}")
    print(f"Lowest Closing Price: {df['Close'].min():.2f}")

    print("\nSaving processed data...")
    df.to_csv('gold_price_history.csv')

if __name__ == '__main__':
    main()
