import streamlit as st
import dim_reducer as dr
import encoder as enc
import mssng_vals_hndl as mvh
import outlier_handler as oh
import scaler as sc
import pandas as pd

# Apply Or Skip Scaling
def apply_scaling(df,ind_cols,dep_var) -> pd.DataFrame:
    #checkbox for scaling process
    scaling_choice = st.radio(
        "What do you want to do?",
        ["Apply Scaling", "Skip"],
    )
    if scaling_choice == "Apply Scaling":
        sc_df = sc.app(df,ind_cols,dep_var)
        return sc_df
    else:
        return df

# Apply or skip Dimensionality Reduction
def apply_dim_red(df,dep_var,is_class_or_reg) -> pd.DataFrame:
    #checkbox for dimensionality reduction process
    dim_red_choice = st.radio(
        "What do you want to do?",
        ["Apply Dimensionality Reduction", "Skip"],
    )
    if dim_red_choice == "Apply Dimensionality Reduction":
        dr_df = dr.app(df,dep_var,is_class_or_reg)
        return dr_df
    else:
        return df

def app(df,dep_var,is_class_or_reg,ind_cols) -> pd.DataFrame:
    st.header('Data Preprocessing Suite', divider="blue")
    #necessary processes
    #missing value handling process
    mvh_df = mvh.app(df)
    #handling outliers
    oh_df = oh.app(mvh_df)
    #encoding data
    enc_df = enc.app(oh_df,[dep_var])
    sc_df = apply_scaling(enc_df,ind_cols,dep_var)
    dim_red_df = apply_dim_red(sc_df,dep_var,is_class_or_reg)
    return dim_red_df