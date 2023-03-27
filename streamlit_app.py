

# data=pd.read_csv('Tesla.csv - Tesla.csv.csv')


    
    
import streamlit as st
import pandas as pd


# Veri dosyasını oku
df = pd.read_csv('Tesla.csv - Tesla.csv.csv')

# Create figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

# Set layout
fig.update_layout(title='Tesla Stock Price',
                   yaxis_title='Price (USD)',
                   xaxis_rangeslider_visible=True)

# Plot figure
st.plotly_chart(fig)



# Close kolonunu ve State kolonunu içeren yeni bir DataFrame oluştur
new_df = pd.DataFrame()
new_df['Close'] = df['Close']
new_df['State'] = ''

# Interaktif tabloyu sayfaya ekle
#st.table(new_df)
st.experimental_data_editor(new_df)

