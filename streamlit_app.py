from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objs as go

"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""

# data=pd.read_csv('Tesla.csv - Tesla.csv.csv')


    
    



# Data.csv dosyasını okuyoruz
df = pd.read_csv("Tesla.csv")

# Mum grafik oluşturuyoruz
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

# Zoom yapabilmek için layout ayarlarını yapıyoruz
fig.update_layout(
    xaxis_rangeslider_visible=True,
    xaxis_title="Tarih",
    yaxis_title="Fiyat"
)

# Mum grafik arayüzünü gösteriyoruz
st.plotly_chart(fig)

# Close ve State kolonlarını seçiyoruz
df = df[["Close", "State"]]

# State kolonuna el ile veri girişi yapabilirsiniz

# Yeni bir sütun ekliyoruz ve bu sütunda her bir kapanış değerinin yüzde değişimini hesaplıyoruz
df["Close % Change"] = df["Close"].pct_change()

# Tablo arayüzünü gösteriyoruz
st.write(df)
