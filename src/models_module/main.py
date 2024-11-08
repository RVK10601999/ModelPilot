import streamlit as st
import num_models as nm
from sklearn.model_selection import train_test_split

def app(df,indep_cols,dep_var,test_size):
    x = df[indep_cols].values
    y = df[dep_var].values
    xtr,xts,ytr,yts = train_test_split(x, y, test_size=test_size, random_state=123)
    fitted_model = nm.app(xtr,xts)
    fitted_model