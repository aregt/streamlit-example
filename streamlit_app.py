from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objs as go
pip install plotly

# data=pd.read_csv('Tesla.csv - Tesla.csv.csv')


    
    
import streamlit as st
import pandas as pd
import plotly.express as px

# Veri dosyasını oku
df = pd.read_csv('Tesla.csv')

# Mum grafiğini oluştur
fig = px.candlestick(df, x='Date', open='Open', high='High', low='Low', close='Close')
fig.update_layout(xaxis_rangeslider_visible=False)

# Grafiği sayfaya ekle
st.plotly_chart(fig)

# Close kolonunu ve State kolonunu içeren yeni bir DataFrame oluştur
new_df = pd.DataFrame()
new_df['Close'] = df['Close']
new_df['State'] = ''

# Interaktif tabloyu sayfaya ekle
st.table(new_df)
