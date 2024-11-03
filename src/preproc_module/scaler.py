from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
import streamlit as st
import pandas as pd
import numpy as np

def scaler(xtr,xts,ytr,yts):
    # Create a StandardScaler instance
    stdsclr = StandardScaler()
    # Fit and transform the data
    sc_xtr = stdsclr.fit_transform(xtr)
    sc_xts = stdsclr.transform(xts)
    new_df = pd.concat([pd.DataFrame(sc_xtr),pd.DataFrame(sc_xts)],axis=0)
    new_df['target'] = pd.concat([ytr,yts],axis=0)
    return new_df

def normer(xtr,xts,ytr,yts):
    # Create a MinMaxScaler instance
    mnmxsclr = MinMaxScaler()
    # Fit and transform the data
    sc_xtr = mnmxsclr.fit_transform(xtr)
    sc_xts = mnmxsclr.transform(xts)
    new_df = pd.concat([pd.DataFrame(sc_xtr),pd.DataFrame(sc_xts)],axis=0)
    new_df['target'] = pd.concat([ytr,yts],axis=0)
    return new_df

def app(df,indep_cols,dep_var):
    scaling_choice = st.radio(
        "What do you want to do?",
        ["Normalization", "Standardization"],
    )
    test_size = st.number_input(label=f'Test data size for Scaling',placeholder='Select Value',min_value=0.05, max_value=0.45, value=0.2)
    x = df[indep_cols].values
    y = df[dep_var].values
    xtr,xts,ytr,yts = train_test_split(x, y, test_size=test_size, random_state=123)
    if scaling_choice == "Normalization":
        sc_xtr,sc_xts = normer(xtr,xts)
    else:
        sc_xtr,sc_xts = scaler(xtr,xts)
    return sc_xtr


