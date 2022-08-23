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
cuzdanTL=10000
alim_orani=0.1
karAl_orani=0.15


islem_Listesi=np.array([])
islem_Listesi_alim_fiyatlari=np.array([])
alim=0
islem_Listesi_alim_fiyatlari=islem_Listesi*islem_Listesi_alim_fiyatlari

with st.echo(code_location='below'):
    a=3
    
