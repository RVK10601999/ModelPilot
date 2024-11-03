import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import pandas as pd

def do_pca(x,y,indep_cols,test_size=0.2) -> pd.DataFrame:
    xtr,xts,ytr,yts = train_test_split(x, y, test_size=test_size, random_state=123)
    n_comps = st.number_input(label=f'No. of Components after PCA',placeholder='Select Value. Note: MAXIMUM VALUE ALLOWED MUST BE LESSER THAN THE NO. OF COLUMNS',min_value=0, max_value=len(indep_cols)-1, value=0.2)
    pca = PCA(n_components=n_comps)
    pc_xtr = pca.fit_transform(xtr)
    pc_xts = pca.transform(xts)
    new_df = pd.concat([pd.DataFrame(pc_xtr),pd.DataFrame(pc_xts)],axis=0)
    new_df['target'] = pd.concat([ytr,yts],axis=0)
    return new_df

def do_lda(x,y,indep_cols,test_size=0.2) -> pd.DataFrame:
    xtr,xts,ytr,yts = train_test_split(x, y, test_size=test_size, random_state=123)
    le = LabelEncoder()
    y = le.fit_transform(y)
    n_comps = st.number_input(label=f'No. of Components after LDA',placeholder='Select Value. Note: MAXIMUM VALUE ALLOWED MUST BE LESSER THAN THE NO. OF COLUMNS',min_value=0, max_value=len(indep_cols)-1, value=0.2)
    lda = LDA(n_components=n_comps)
    ld_xtr = lda.fit_transform(xtr, ytr)
    ld_xts = lda.transform(xts)
    new_df = pd.concat([pd.DataFrame(ld_xtr),pd.DataFrame(ld_xts)],axis=0)
    new_df['target'] = pd.concat([ytr,yts],axis=0)
    return new_df


def app(df,dep_var,is_class_or_reg) -> pd.DataFrame:
    indep_cols = [c for c in df.columns if c not in [dep_var]]
    test_size = st.number_input(label=f'Test data size for Dimensionality Reduction Algo',placeholder='Select Value',min_value=0.05, max_value=0.45, value=0.2)
    x = df[indep_cols].values
    y = df[dep_var].values
    if is_class_or_reg == "Categorical":
        return do_lda(x,y,indep_cols,test_size)
    else:
        return do_pca(x,y,indep_cols,test_size)