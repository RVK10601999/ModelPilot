import streamlit as st
import csv_selector,preloader,random_data_giver

st.header('Data Generator', divider="blue")

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

if genre == "Use pre-loaded datasets":
    df = preloader.app()
elif genre == "Load a CSV file":
    df = csv_selector.app()
else:
    df = random_data_giver.app()