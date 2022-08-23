from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import datetime as dt


#import yfinance as yf
#data = yf.download('MSFT', start = '2012-01-01', end='2017-01-01')


link="https://www.kaggle.com/datasets/rpaguirre/tesla-stock-price?select=Tesla.csv+-+Tesla.csv.csv"
data=pd.read_csv("link")




with st.echo(code_location='below'):
    cuzdanTL=st.slider("Cüzdan Bakiyesi",0,10000,step=500)
    alim_orani=st.number_input("Yeni Alım Oranı")
    karAl_orani=st.number_input("Kar alma Oranı")
    a=3
    
    
    
