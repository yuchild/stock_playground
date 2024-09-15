#!usr/bin/env python3

import pandas as pd
import numpy as np
from yfinance import Ticker
from pykalman import KalmanFilter

def download(symbol,interval,period):
    stock = Ticker(symbol)
    stock_df = stock.history(interval=interval,
                             period=period,
                             auto_adjust=False,
                             prepost=True, # include aftermarket hours
                            )
    stock_df.to_pickle(f'./data/{symbol}_{interval}_df.pkl')
    
def load(symbol,interval):
    return pd.read_pickle(f'./data/{symbol}_{interval}_df.pkl')


























if __name__ == '__main__':
    ...




