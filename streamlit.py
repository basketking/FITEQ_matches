import streamlit as st
import pandas as pd

df_finalstats = pd.read_excel('https://github.com/basketking/FITEQ_matches/blob/main/finalstats.xlsx?raw=true')
df_teq_score = pd.read_excel('https://github.com/basketking/FITEQ_matches/blob/main/teq_score.xlsx')


st.table(df_finalstats)