import inspect
import streamlit as st
from sklearn import linear_model

def app(xtr,xts):
    regression_models = [
        "LinearRegression", "Ridge", "Lasso", "ElasticNet", "Lars", "LassoLars", "OrthogonalMatchingPursuit",
        "BayesianRidge", "ARDRegression", "HuberRegressor", "PassiveAggressiveRegressor", "RANSACRegressor",
        "TheilSenRegressor", "QuantileRegressor"
    ]
    model_name = st.radio(
        "What model would you like to use?",
        options=regression_models,
        captions=regression_models
    )
    model_class = getattr(linear_model, model_name)
    model_instance = model_class()
    trained_model = model_instance.fit(xtr,xts)
    return trained_model
