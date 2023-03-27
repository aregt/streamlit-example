

# data=pd.read_csv('Tesla.csv - Tesla.csv.csv')


    
    
import streamlit as st
import pandas as pd
#import plotly.express as px

# Veri dosyasını oku
df = pd.read_csv('Tesla.csv - Tesla.csv.csv')



########################

# Mum grafik oluşturma
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)
fig.add_trace(go.Candlestick(x=df["Date"],
                             open=df["Open"],
                             high=df["High"],
                             low=df["Low"],
                             close=df["Close"]),
              row=1, col=1)
fig.update_xaxes(title_text="Tarih")

# Zoom ve pan yapabilmek için figür ayarları
fig.update_layout(dragmode="zoom",
                  xaxis_rangeslider_visible=False)

# Grafik ve tablo gösterimi
st.plotly_chart(fig)
st.write("## Veri Tablosu")
state_list = df["State"].unique().tolist()
state = st.selectbox("State", state_list)


########################




# Mum grafiğini oluştur
#fig = px.candlestick(df, x='Date', open='Open', high='High', low='Low', close='Close')
#fig.update_layout(xaxis_rangeslider_visible=False)

# Grafiği sayfaya ekle
# st.plotly_chart(fig)

# Close kolonunu ve State kolonunu içeren yeni bir DataFrame oluştur
new_df = pd.DataFrame()
new_df['Close'] = df['Close']
new_df['State'] = ''

# Interaktif tabloyu sayfaya ekle
#st.table(new_df)
st.experimental_data_editor(new_df)

