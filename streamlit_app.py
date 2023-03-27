

# data=pd.read_csv('Tesla.csv - Tesla.csv.csv')


    

import plotly.graph_objs as go
import pandas as pd
import streamlit as st

# Veri dosyasını oku
df = pd.read_csv('Tesla.csv - Tesla.csv.csv')

# Mum grafiği oluştur
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

# Düzenleme yap
fig.update_layout(title='Tesla Hisse Senedi Fiyatları',
                   yaxis_title='Fiyat (USD)',
                   xaxis_rangeslider_visible=True)

# Grafiği göster
st.plotly_chart(fig)



# Close kolonunu ve State kolonunu içeren yeni bir DataFrame oluştur
new_df = pd.DataFrame()
new_df['Close'] = df['Close']
new_df['State'] = ''

# Interaktif tabloyu sayfaya ekle
#st.table(new_df)
st.experimental_data_editor(new_df)

