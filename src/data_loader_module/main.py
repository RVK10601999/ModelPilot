import streamlit as st
from data_loader_module import csv_selector as cs
from data_loader_module import preloader as pl
from data_loader_module import random_data_giver as rdg
import pandas as pd
from typing import Tuple,List

def app() -> Tuple[pd.DataFrame, str, str, List]:
    st.header('Page 1 - Data Preparation Suite', divider="blue")

    #radio selector for data selecting data loading process
    genre = st.radio(
        "What do you want to do?",
        ["Generate random data", "Load a CSV file", "Use pre-loaded datasets"],
        captions=[
            "Generate custom data using the built-in random data generator suite.",
            "Use your own file from your local system.",
            "Use Available datasets from scikit-learn's suite of datasets.",
        ],
    )

    dependent_type = st.radio(
        "What is the kind of data?",
        ["Numerical", "Categorical"],
        captions=[
            "Numerical Dependent variable",
            "Categorical Dependent variable"
        ],
    )
    if genre == "Use pre-loaded datasets":
        df,dep_var = pl.app() or (pd.DataFrame(),'none')
    elif genre == "Load a CSV file":
        df,dep_var = cs.app()
    else:
        df,dep_var = rdg.app(dependent_type)
    
    return df,dep_var,dependent_type,[c for c in df.columns if c not in [dep_var]]