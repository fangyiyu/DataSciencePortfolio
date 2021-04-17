import datetime
import glob
import logging
import os
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.offline as opy
from binance.client import Client
import plotly.offline as py
from prophet import Prophet

logger = logging.getLogger(__name__)


def data():
    client = Client('V6GT0mgwDWIqHzeCxlmJn0Q3BZPD9BCujEcobzr6Obz35leYAudRmGOrwsirof4U', 'uSaG10U4pgqKWD9WfoYbGCoXEAwn2XTkixIQlqL6h4Q6kWw3kFkRtCGXSFxhLZj1')

# Pull bitcoin data from Binance API
    symbol = 'BTCUSDT'
    BTC = client.get_historical_klines(symbol=symbol, interval = Client.KLINE_INTERVAL_1DAY  , start_str = '1 year ago UTC')
    BTC = pd.DataFrame(BTC, columns=['Open time','Open','High','Low','Close','Volume','Close time','Quote asset volume','Number of trades','Taker buy base asset volume','Taker buy quote asset volume','ignored'])
    BTC['Open time'] = pd.to_datetime(BTC['Open time'], unit='ms')
    df_new=BTC[['Open time','Close']]

# Simple data preprocessing
    df_new=df_new.rename(columns={'Open time':'ds','Close':'y'})
    df_new['y'] = df_new['y'].astype(float)
    df_old = df_new.copy()
    df_new['y'] = np.log(df_new['y'])

    return (df_new, df_old)


def predict():

        # Build model
    m=Prophet(interval_width=0.95, yearly_seasonality=True, weekly_seasonality=True,daily_seasonality=True, changepoint_prior_scale=2)
    m.add_seasonality(name='monthly', period=30.5, fourier_order=5, prior_scale=0.02)
    df_new = data()[0]
    m.fit(df_new)
    future = m.make_future_dataframe(periods = 7,freq='D')

        # Predict
    forecast = m.predict(future)
    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    forecast['yhat'] = np.exp(forecast['yhat'])
    forecast['yhat_lower'] = np.exp(forecast['yhat_lower'])
    forecast['yhat_upper'] = np.exp(forecast['yhat_upper'])

    return forecast


def graph():
    forecast = predict()
    x = np.array(forecast['ds'], dtype='datetime64[D]')
    y = np.array(forecast['yhat'])
    plot_div = plot([go.Scatter(x=x, y=y,
    mode='lines', name='Bitcoin price',
    opacity=0.8, marker_color='#7F7F7F')],
    output_type='div', include_plotlyjs=False, show_link=False, link_text="")

    return plot_div


