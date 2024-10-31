from sklearn.preprocessing import MinMaxScaler,StandardScaler
import streamlit as st

def scaler(xtr):
    scaler_type = st.radio(
        "What type of scaling you want to use?",
        ["MinMaxScaler", "StandardScaler"],
        captions=[
            "Use MinMaxScaler",
            "Use StandardScaler"
        ],
    )
    if scaler_type=='MinMaxScaler':
        # Create a MinMaxScaler instance
        mnmxsclr = MinMaxScaler()
        # Fit and transform the data
        sc_xtr = mnmxsclr.fit_transform(xtr)
    else:
        # Create a StandardScaler instance
        stdsclr = StandardScaler()
        # Fit and transform the data
        sc_xtr = stdsclr.fit_transform(xtr)
    return sc_xtr