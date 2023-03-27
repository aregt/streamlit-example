

# data=pd.read_csv('Tesla.csv - Tesla.csv.csv')


    
    
import streamlit as st
import pandas as pd
#import plotly.express as px

# Veri dosyasını oku
df = pd.read_csv('Tesla.csv - Tesla.csv.csv')

# Close kolonunu ve State kolonunu içeren yeni bir DataFrame oluştur
new_df = pd.DataFrame()
new_df['Close'] = df['Close']
new_df['State'] = ''

# Interaktif tabloyu sayfaya ekle
#st.table(new_df)
st.experimental_data_editor(new_df)

