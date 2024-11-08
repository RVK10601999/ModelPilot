from data_loader_module import main as dlm_app
from preproc_module import main as ppm_app
import streamlit as st

# Initialize the session state for tracking the current page
if 'page' not in st.session_state:
    st.session_state.page = 1

# Function to display top 5 rows
def display_df(df):
    st.write('Displaying Top 5 rows....')
    st.write(df.head())

# Function to go to the next page
def next_page():
    if st.session_state.page < 4:
        st.session_state.page += 1

# Function to go to the previous page
def prev_page():
    if st.session_state.page > 1:
        st.session_state.page -= 1

# Display content based on the current page
if st.session_state.page == 1:
    #PAGE1
    df,dep_var,dependent_type,indep_ls = dlm_app.app()
    st.session_state.df = df
    st.session_state.dep_var = dep_var
    st.session_state.dependent_type = dependent_type
    st.session_state.indep_ls = indep_ls
    st.button("Next", on_click=next_page)

elif st.session_state.page == 2:
    #PAGE2
    processed_df = ppm_app.app(st.session_state.df,st.session_state.dep_var,st.session_state.dependent_type,st.session_state.indep_ls)
    st.session_state.processed_df = processed_df
    display_df(st.session_state.processed_df)
    st.button("Previous", on_click=prev_page)
    st.button("Next", on_click=next_page)

elif st.session_state.page == 3:
    st.title("Page 3")
    st.write("Welcome to Model Building Page")
    st.button("Previous", on_click=prev_page)
    st.button("Next", on_click=next_page)

elif st.session_state.page == 4:
    st.title("Page 4")
    st.write("Welcome to Model Pickler Page")
    st.button("Previous", on_click=prev_page)
    st.button("Restart", on_click=lambda: st.session_state.update({"page": 1}))
