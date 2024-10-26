import streamlit as st
import pandas as pd
import data_loader_utils as dlu

def app():
    '''function to load csv file(supports selecting multiple files)'''
    uploaded_files = st.file_uploader(
        "Choose any number of CSV files", accept_multiple_files=True
    )

    df = pd.DataFrame([])
    for uploaded_file in uploaded_files:
        df = pd.concat([df,pd.read_csv(uploaded_file)])
    return df,dlu.get_dependent_var_widget(df)