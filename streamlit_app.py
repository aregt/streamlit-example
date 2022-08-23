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
cuzdanTL=st.slider("Cüzdan Bakiyesi"0,10000,step=500)
alim_orani=0.1
karAl_orani=0.15


islem_Listesi=np.array([])
islem_Listesi_alim_fiyatlari=np.array([])
alim=0
islem_Listesi_alim_fiyatlari=islem_Listesi*islem_Listesi_alim_fiyatlari

for i in data["Close"]:
    if len(islem_Listesi)==0:
        alim=round((alim_orani*cuzdanTL)/i)
        islem_Listesi=np.append(islem_Listesi,alim)
        islem_Listesi_alim_fiyatlari=np.append(islem_Listesi_alim_fiyatlari,i)
    print(i)

with st.echo(code_location='below'):
    a=3
    
