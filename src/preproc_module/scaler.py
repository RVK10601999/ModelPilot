from sklearn.preprocessing import MinMaxScaler,StandardScaler
import streamlit as st

def scaler(xtr):
    # Create a StandardScaler instance
    stdsclr = StandardScaler()
    # Fit and transform the data
    sc_xtr = stdsclr.fit_transform(xtr)
    return sc_xtr


def normer(xtr):
    # Create a MinMaxScaler instance
    mnmxsclr = MinMaxScaler()
    # Fit and transform the data
    sc_xtr = mnmxsclr.fit_transform(xtr)
    return sc_xtr

def app(xtr):
    scaling_choice = st.radio(
        "What do you want to do?",
        ["Normalization", "Standardization"],
    )
    if scaling_choice == "Normalization":
        sc_xtr = normer(xtr)
    else:
        sc_xtr = scaler(xtr)
    return sc_xtr


