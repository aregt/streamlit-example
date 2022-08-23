from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import datetime as dt

"""Data İmport"""

#import yfinance as yf
#data = yf.download('MSFT', start = '2012-01-01', end='2017-01-01')
link="https://www.kaggle.com/datasets/rpaguirre/tesla-stock-price?select=Tesla.csv+-+Tesla.csv.csv"

data=pd.read_csv("link")
# Welcome to Streamlit!

#Edit `/streamlit_app.py` to customize this apsp to your heart's desire :heart:

#If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
#forums](https://discuss.streamlit.io).

#In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    cuzdanTL=st.slider("Cüzdan Bakiyesi",0,10000,step=500)
    alim_orani=st.number_input("Yeni Alım Oranı")
    karAl_orani=st.number_input("Kar alma Oranı")
    a=3
    
    
    
