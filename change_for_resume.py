import requests
import pandas as pd
import plotly.express as px
import json
import streamlit as st

def send_resume(salary, min_salary, df_main, bytes_data, num_vacanc):
    if bytes_data is None or bytes_data.empty:
        # Обработка df_main
        if salary:
            df = df_main.dropna(subset=['salary_from'])
            df = df[df['salary_from'] >= min_salary]
        else:
            df = df_main[pd.isna(df_main['salary_from'])]
        
        df = df.head(num_vacanc)
        df = list(df['apply_alternate_url'])
        
    else:
        # Обработка bytes_data
        if len(bytes_data.columns) > 1:
            st.write('Wrong number of columns, there should be one column with links')
            df = pd.DataFrame()  # Возвращаем пустой DataFrame
        else:
            df = list(bytes_data)

    return df

def view_resume(salary, min_salary, df_main, bytes_data=None, num_vacanc=10):
    if bytes_data is None or bytes_data.empty:
        # Обработка df_main
        if salary:
            df = df_main.dropna(subset=['salary_from'])
            df = df[df['salary_from'] >= min_salary]
        else:
            df = df_main[pd.isna(df_main['salary_from'])]
        
        df = df.head(num_vacanc)
        df = df[['name','apply_alternate_url', 'salary_from','employer_name']].reset_index(drop=True)
        
    else:
        # Обработка bytes_data
        if len(bytes_data.columns) > 1:
            st.write('Wrong number of columns, there should be one column with links')
            df = pd.DataFrame()  # Возвращаем пустой DataFrame
        else:
            df = bytes_data.head(num_vacanc)

    return df