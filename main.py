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

    return df

def calculate_price_metrics(df):

# calculate various price metrics

    # calculate daily price change
    df['Daily_Return'] = df['Close'].pct_change()

