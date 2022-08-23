from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""

data=pd.read_csv('Tesla.csv - Tesla.csv.csv')

cuzdanTL=st.slider("Cüzdan Bakiyesi",0,10000,step=500)
alim_orani=st.number_input("Alım Oranı % (cüzdan bakiyesinin % kaçıyla alım yapsın)",value=0.1)
karAl_orani=st.number_input("Kar Alma Oranı %",value= 0.2)


islem_Listesi=np.array([])  # her bir eleman alınan hisse adetidir
islem_Listesi_alim_fiyatlari=np.array([])
al=0


for i in data["Close"]:
    if len(islem_Listesi)==0:
        al=round((alim_orani*cuzdanTL)/i)  # alınan hisse sayısı
        islem_Listesi=np.append(islem_Listesi,al)
        islem_Listesi_alim_fiyatlari=np.append(islem_Listesi_alim_fiyatlari,i)
        islem_Listesi_alim_bakiyeleri=islem_Listesi*islem_Listesi_alim_fiyatlari
        cuzdanTL=cuzdanTL-(al*i)
    #elif 
     
 

st.write("İşlem Listesi (Her bir adet):  ", islem_Listesi)
st.write("İşlem alınan fiyatları:  ", islem_Listesi_alim_fiyatlari)
st.write("Her bir işlem için ödenen para:  ", islem_Listesi_alim_bakiyeleri)
st.write("Cüzdanda Kalan Para:\n  ", cuzdanTL)
    

with st.echo(code_location='below'):
    a=3
    
    
