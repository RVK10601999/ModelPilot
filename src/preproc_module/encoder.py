from sklearn.preprocessing import LabelEncoder


def app(df,c_ls) -> pd.DataFrame:
    label_encoder = LabelEncoder()
    for c in c_ls:
        df[c]= label_encoder.fit_transform(df[c])
    return df