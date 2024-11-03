import streamlit as st
import pandas as pd


def get_dependent_var_widget(df) -> str:
    # Used to pass on what is/are dependent & independent variables to the next page
    dep_var_choice = st.radio(
        "Select dependent variable",
        list(df.columns)
    )
    if df.shape[0]:
        st.write("Displaying top 5 rows")
        st.write(df.head())
    return dep_var_choice