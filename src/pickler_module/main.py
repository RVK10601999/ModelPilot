from pickler_module import pickler as pklr
import streamlit as st

def app(model):
    st.header('Page 4 - Model Exporting Suite', divider="blue")
    pklr.app(model)
