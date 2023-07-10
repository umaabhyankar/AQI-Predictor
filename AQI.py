# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 22:15:15 2023

@author: umaab
"""

import pandas as pd
import streamlit as st
import datetime

st.set_page_config(layout="wide", page_title="Air Quality Index")

@st.experimental_memo
def load_data():

    path = 'https://github.com/umaabhyankar/AQI-Predictor/raw/main/data/solapur_india_air_quality.csv'

    data = pd.read_csv(path)

    return data

@st.experimental_memo
def filterdata(df, date_selected):
    return df[df["date"] == date_selected]

data = load_data()

row1_1, row1_2 = st.columns((2, 3))

if not st.session_state.get("url_synced", False):
    try:
        AQI_date = int(st.experimental_get_query_params()["AQI_date"][0])
        st.session_state["AQI_date"] = AQI_date
        st.session_state["url_synced"] = True
    except KeyError:
        pass
    
def update_query_params():
    date_selected = st.session_state["AQI_date"]
    st.experimental_set_query_params(AQI_date=date_selected)
    
with row1_1:
    st.title("Air Quality Index")
    date_selected = st.date_input(
    "Select date",
    datetime.date(2019, 7, 6), key="AQI_date", on_change=update_query_params)
    
with row1_2:
    st.write(
        """
    ##
    Predicting Air Quality for the next three days.
    """
    )