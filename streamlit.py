import streamlit as st
import pandas as pd

df_finalstats = pd.read_csv('https://github.com/basketking/FITEQ_matches/raw/main/finalstats.csv', error_bad_lines=False)


df_teq_score = pd.read_csv('https://github.com/basketking/FITEQ_matches/blob/main/teq_score.csv', error_bad_lines = False)


st.dataframe(df_finalstats)