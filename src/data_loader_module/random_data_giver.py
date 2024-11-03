import streamlit as st
import pandas as pd
from random import randint,choice
import data_loader_utils as dlu
from typing import List,Tuple

def generate_random_numbers(min_value, max_value, length) -> List:
    '''generate randomly distributed nu,bers between minimu & maximum values based on the row count'''
    return [randint(min_value, max_value) for _ in range(length)]

def generate_random_classes(length,class_length) -> List:
    '''generate randomly distributed classes based on the row count'''
    strings = [f'class_{_}' for _ in range(class_length)]
    return [choice(strings) for _ in range(length)]

def app(dependent_type) -> Tuple[pd.DataFrame, List]:
    '''Random Data Generator : \n1. includes row count in decision making
\n2. function to generate independent variables
\n3. function to generate & load random data

    '''
    df = pd.DataFrame()
    row_count = st.number_input(label='Count of Rows',placeholder='Select No. of rows',value=10,min_value=10)
    col_count = st.number_input(label='Count of Columns',placeholder='Select No. of columns',value=1,min_value=1)
    for c in range(0, col_count):
        min_val = st.number_input(label=f'Minimum Value for column#{c}',placeholder='Select Minimum Value',value=0)
        max_val = st.number_input(label=f'Maximum Value for column#{c}',placeholder='Select Maximum Value',value=100)
        df[f'column#{c}'] = pd.DataFrame(generate_random_numbers(min_val, max_val, row_count))
    if dependent_type=='Numerical':
        min_val = st.number_input(label=f'Minimum Value for target',placeholder='Select Minimum Value',value=0)
        max_val = st.number_input(label=f'Maximum Value for target',placeholder='Select Maximum Value',value=100)
        df['target'] = pd.DataFrame(generate_random_numbers(min_val, max_val, row_count))
    else:
        cat_count = st.number_input(label=f'No. of categories for target',placeholder='Select No. of classes',value=2,min_value=2)
        df['target'] = pd.DataFrame(generate_random_classes(row_count,cat_count))

    return df,dlu.get_dependent_var_widget(df)

