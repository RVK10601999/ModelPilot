import streamlit as st
import pandas as pd
import numpy as np

def app(df):
    for c in df.columns:
        if df[c].dtypes == 'float64' or df[c].dtypes == 'int64':
            df.loc[df[c].isna(),c] = np.mean(df.loc[~df[c].isna(),c])
    for c in df.columns:
        if df[c].dtypes != 'float64' or df[c].dtypes != 'int64':
            df = df.loc[~df[c].isna()]
    return df