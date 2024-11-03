import streamlit as st
import dim_reducer as dr
import encoder as enc
import mssng_vals_hndl as mvh
import outlier_handler as oh
import scaler as sc

def app(df,dep_var,is_class_or_reg,ind_cols):
    #necessary processes
    #missing value handling process
    mvh_df = mvh.app(df)
    #handling outliers
    oh_df = oh.app(mvh_df)
    #encoding data
    enc_df = enc.app(oh_df,[])
    # Apply Scaling
    def apply_scaling(df,ind_cols,dep_var):
        #checkbox for scaling process
        scaling_choice = st.radio(
            "What do you want to do?",
            ["Apply Scaling", "Skip"],
        )
        if scaling_choice == "Apply Scaling":
            dr_df = sc.app(df[ind_cols])
            return dr_df
        else:
            return df
    scld_df = apply_scaling(enc_df,ind_cols,dep_var)
    # Apply or skip Dimensionality Reduction
    def apply_dim_red(df,dep_var,is_class_or_reg):
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
    dim_red_df = apply_dim_red(scld_df,dep_var,is_class_or_reg)
    return dim_red_df


# st.header('Data Preprocessing Suite', divider="blue")

# def apply_dim_red(df,dep_var,is_class_or_reg):
#     #checkbox for dimensionality reduction process
#     dim_red_choice = st.radio(
#         "What do you want to do?",
#         ["Apply Dimensionality Reduction", "Skip"],
#     )
#     if dim_red_choice == "Apply Dimensionality Reduction":
#         dr_df = dr.app(df,dep_var,is_class_or_reg)
#     elif dim_red_choice == "skip":
#         dr_df = dr.app(df,dep_var,is_class_or_reg)
#     return dr_df

# #necessary processes
# #missing value handling process
# mvh_df = mvh.app(df)
# #handling outliers
# oh_df = oh.app(mvh_df)
# #encoding data
# enc_df = enc.app(oh_df,[])

# #radio for scaling process
# scaling_choice = st.radio(
#     "What do you want to do?",
#     ["Apply Normalization", "Apply Scaling"],
# )

# dim_red_choice = st.checkbox(
#     "What do you want to do?",
#     ["Apply Dimensionality Reduction"],
# )


# if scaling_choice == "Apply Normalization":
#     sc_df = sc.normer(df)
#     apply_dim_red(df,dep_var,is_class_or_reg)

# elif scaling_choice == "Apply Scaling":
#     sc_df = sc.scaler(df)