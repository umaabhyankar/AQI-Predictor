import json
import time
import pickle
import joblib
import pandas as pd

import hopsworks 
import streamlit as st
import datetime

import plotly.express as px
import folium
from streamlit_folium import st_folium

import datetime
import time
import requests
import json

import numpy as np
import pandas as pd
import folium
import os

import warnings
warnings.filterwarnings("ignore")

CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1

def print_fancy_header(text, font_size=22, color="#ff5f27"):
    res = f'<span style="color:{color}; font-size: {font_size}px;">{text}</span>'
    st.markdown(res, unsafe_allow_html=True)

@st.experimental_memo
def get_feature_view(td_version):
    feature_view = fs.get_feature_view(
        name = 'air_quality_fv',
        version = 1
    )

    air_quality_fg_api = fs.get_or_create_feature_group(
    name = 'air_quality_fg_api',
    version = 1
    )

    query = air_quality_fg_api.select_all()

    feature_view = fs.get_or_create_feature_view(
    name='air_quality_fv_api',
    version=1,
    query=query
    )

    X_api, _ = feature_view.get_training_data(
    training_dataset_version=td_version
    )

    return X_api

st.title(':partly_sunny_rain: Air Quality Index :partly_sunny_rain:')

st.subheader("Today's date: " + str(datetime.date.today()))

project = hopsworks.login()
fs = project.get_feature_store()

X_api = get_feature_view(1)

X_api.sort_values('date', inplace=True)

X_api['date'] = pd.to_datetime(X_api['date']).dt.tz_localize(None)

X_api = X_api.loc[X_api['date']>pd.to_datetime('today')]

mr = project.get_model_registry()

retrieved_model = mr.get_model(
    name="air_quality_xgboost_model",
    version=1
)

saved_model_dir = retrieved_model.download()

retrieved_xgboost_model = joblib.load(saved_model_dir + "/xgboost_regressor.pkl")

X_prediction = X_api[['pm25', 'pm10', 'o3', 'no2', 'so2', 'co', 'aqi']]

y_prediction = X_prediction.pop('aqi')

predictions = retrieved_xgboost_model.predict(X_prediction)

X_api['predictions'] = predictions

X_api.sort_values('date', inplace=True)

X_api['date'] = pd.to_datetime(X_api['date']).dt.tz_localize(None)

X_api = X_api.loc[X_api['date']>pd.to_datetime('today')]

X_api = X_api[['date', 'predictions']]

X_api['predictions'] = [int(i) for i in X_api.predictions]

X_api.rename(columns={'date': 'Date', 'predictions': 'Air Quality Index'}, inplace=True)

st.table(X_api)

X_api = X_api.set_index('Date')

st.line_chart(X_api)
