import streamlit as st
import pandas as pd
from sklearn import datasets

def get_datasets(d):
    # Use dir() to get all attributes of the sklearn.datasets module
    dataset_functions = dir(d)
    # Filter functions that start with "load_" or "fetch_"
    dataset_functions = [f for f in dataset_functions if f.startswith("load_") or f.startswith("fetch_")]
    return dataset_functions

def load_dataset(datasets,dataset_name):
    # Check if the dataset_name exists in sklearn.datasets
    df = pd.DataFrame()
    #checks if selected dataset is available
    if hasattr(datasets, dataset_name):
        # Get the function dynamically
        dataset_func = getattr(datasets, dataset_name)
        data = dataset_func()
        #extract independent variables
        df[data['feature_names']] = data['data']
        #extract dependent variables
        df['target'] = data['target']
        #return extracted dataframe
        return df
    #selected data is unavailable
    else:
        #return empty dataframe
        return df


def app():
    dataset_names = get_datasets(d=datasets)
    # Display the filtered dataset functions
    st.write("Available Datasets in sklearn.datasets:")
    #select-box to display available datasets
    option = st.selectbox(
    "Which one of these datasets do you need?",
    dataset_names,
    index=None,
    placeholder="Select Dataset...")
    #load selected dataset and display sample
    if option:
        st.write("You selected:", option)
        df = load_dataset(datasets,option)
        if df.shape[0]:
            st.write("Displaying top 5 rows")
            st.write(df.head())
        return df


