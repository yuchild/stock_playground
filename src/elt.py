#!usr/bin/env python3

import pandas as pd
import numpy as np
from yfinance import Ticker
from pykalman import KalmanFilter

<<<<<<< HEAD
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import cross_val_predict


=======
>>>>>>> 0a147dabce0666779a1ae80b75e4d85992e64076
def download(symbol,interval,period):
    stock = Ticker(symbol)
    stock_df = stock.history(interval=interval,
                             period=period,
                             auto_adjust=False,
                             prepost=True, # include aftermarket hours
                            )
    stock_df.columns = stock_df.columns.str.lower().str.replace(' ', '_')
    stock_df.to_pickle(f'./data/{symbol}_{interval}_df.pkl')
    
def load(symbol,interval):
    return pd.read_pickle(f'./data/{symbol}_{interval}_df.pkl')


























if __name__ == '__main__':
    ...




