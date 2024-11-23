import streamlit as st

def app(xtr,xts,models_dc):
    trained_model = None
    model_name = st.radio(
        "What model would you like to use?",
        options=models_dc.keys(),
        captions=models_dc.keys()
    )
    btn_mdl_sub = st.button("Train Selected Model")
    if btn_mdl_sub:
        model_class = models_dc[model_name]
        model_instance = model_class()
        trained_model = model_instance.fit(xtr,xts)
        return trained_model
    return None