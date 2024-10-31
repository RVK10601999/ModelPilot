import streamlit as st
import pandas as pd
import numpy as np

def app(df):
    for c in df.columns:
        print(df[c].dtypes)
        q1 = np.percentile(df[c], 25, method='midpoint')
        q3 = np.percentile(df[c], 75, method='midpoint')
        iqr = q3 - q1
        upper = q3+1.5*iqr
        lower = q1-1.5*iqr
        print(df[df[c] >= upper])
        print(df[df[c] <= lower])
        df.loc[(df[c] >= upper) | (df[c] <= lower),c] = np.mean(df.loc[(df[c] < upper) & (df[c] > lower),c])
    return df