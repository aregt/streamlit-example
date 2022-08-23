from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this apsp to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    cuzdanTL=st.slider("Cüzdan Bakiyesi",0,10000)
    alim_orani=st.number_input("Yeni Alım Oranı",0.01,1)
    karAl_orani=st.number_input("Kar alma Oranı",0.01,1)
    a=3
    
    
    
