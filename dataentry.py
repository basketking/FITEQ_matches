import streamlit as st
import pandas as pd
import numpy as np
import datetime
import streamlit.components.v1 as stc



st.title('Teqball Data Entry Application')

date = st.date_input('Date of the match')

country = st.selectbox("Country of the match", ['Argentina', 'Hungary', 'Portugal' , 'Spain'])

comp_name = st.selectbox('Competition name', ['USA Teqball Tour San Diego', 'Lisbon European Teqball Tour', 'WCHs 2021'])

comp_type = st.selectbox('Competition type', ['Mens Doubles', 'Womens Doubles'])

court_type = st.selectbox('Court type', ['Sand', 'Indoor', 'Outdoor'])


dfdict = {
    'Date' : [] ,
    'Country': [] ,
    'Competition Name': [],
    'Competition Type': [],
    'Court Type' : []
}

df = pd.DataFrame({'Date' : None ,
   'Country': None ,
   'Competition Name': None,
   'Competition Type': None,
   'Court Type' : None}, index = [0])

df_newrowdict = {
   'Date' : date ,
   'Country': country ,
   'Competition Name': comp_name,
   'Competition Type': comp_type,
   'Court Type' : court_type
}

df_newrow = [date, country, comp_name, comp_type, court_type]

if st.button('Submit'):
    df.extend(df_newrow, ignore_index= True )




st.dataframe(df)
