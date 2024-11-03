import streamlit as st
from sklearn.preprocessing import StandardScaler,MinMaxScaler,LabelEncoder
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import pandas as pd
import numpy as np

def do_pca(x,y,indep_cols,test_size=0.2):
    xtr,xts,ytr,yts = train_test_split(x, y, test_size=test_size, random_state=123)
    n_comps = st.number_input(label=f'No. of Components after PCA',placeholder='Select Value. Note: MAXIMUM VALUE ALLOWED MUST BE LESSER THAN THE NO. OF COLUMNS',min_value=0, max_value=len(indep_cols)-1, value=0.2)
    pca = PCA(n_components=n_comps)
    pc_xtr = pca.fit_transform(xtr)
    pc_xts = pca.transform(xts)
    pc_df = pd.DataFrame(pc_xtr)
    pc_df['target'] = y
    return pc_xtr,pc_xts

def do_lda(x,y,indep_cols,test_size=0.2):
    xtr,xts,ytr,yts = train_test_split(x, y, test_size=test_size, random_state=123)
    le = LabelEncoder()
    y = le.fit_transform(y)
    n_comps = st.number_input(label=f'No. of Components after LDA',placeholder='Select Value. Note: MAXIMUM VALUE ALLOWED MUST BE LESSER THAN THE NO. OF COLUMNS',min_value=0, max_value=len(indep_cols)-1, value=0.2)
    lda = LDA(n_components=n_comps)
    ld_xtr = lda.fit_transform(xtr, ytr)
    ld_xts = lda.transform(xts)
    ld_df = pd.DataFrame(ld_xtr)
    ld_df['target'] = y
    return ld_xtr,ld_xts


def app(df,dep_var,is_class_or_reg):
    indep_cols = [c for c in df.columns if c not in [dep_var]]
    test_size = st.number_input(label=f'Test data size for Dimensionality Reduction Algo',placeholder='Select Value',min_value=0.05, max_value=0.45, value=0.2)
    x = df[indep_cols].values
    y = df[dep_var].values
    if is_class_or_reg == "Categorical":
        do_lda(x,y,indep_cols,test_size=0.2)
    else:
        do_pca(x,y,indep_cols,test_size=0.2)