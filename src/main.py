from data_loader_module import main as dlm_app
from preproc_module import main as ppm_app
from models_module import main as mdl_app
from pickler_module import main as pkl_app
from modules.cat_models_params import cat_param_grid
from modules.reg_models_params import regression_model_params
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
    st.session_state.indep_ls = [i for i in st.session_state.processed_df.columns if i!=st.session_state.dep_var]
    st.session_state.number_of_top_models = st.number_input(label="GET TOP N BEST PERFORMING MODEL VIA GRID SEARCH CV METHOD",placeholder="ENTER A NUMBER",min_value=1, max_value=7, value=3)
    st.session_state.top_models = mdl_app.app(st.session_state.processed_df,st.session_state.number_of_top_models,st.session_state.indep_ls,st.session_state.dep_var,st.session_state.dependent_type,cat_param_grid,regression_model_params)
    model_name_ls = [str(list(i.values())) for i in st.session_state.top_models]
    models = [str(list(i.values())[0]) for i in st.session_state.top_models]
    model_zip_dc = dict(zip(model_name_ls,[list(i.values())[0] for i in st.session_state.top_models]))
    print(model_zip_dc)
    print(models)
    print(model_name_ls)
    trained_model = st.radio(
        "What model would you like to use?",
        options=model_name_ls,
        captions=models
    )    
    st.session_state.fitted_model = model_zip_dc[trained_model] 
    st.button("Previous", on_click=prev_page)
    st.button("Next", on_click=next_page)

elif st.session_state.page == 4:
    print(st.session_state.fitted_model)
    fitted_model = st.session_state.fitted_model
    pkl_app.app(fitted_model)
    st.button("Previous", on_click=prev_page)
    st.button("Restart", on_click=lambda: st.session_state.update({"page": 1}))
