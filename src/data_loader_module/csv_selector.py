import streamlit as st
import pandas as pd

#function to load csv file(supports selecting multiple files)
def app():
    uploaded_files = st.file_uploader(
        "Choose only a CSV file", accept_multiple_files=True
    )

    df = pd.DataFrame([])
    for uploaded_file in uploaded_files:
        df = pd.concat([df,pd.read_csv(uploaded_file)])
    if df.shape[0]:
        st.write("Displaying top 5 rows")
        st.write(df.head())