import streamlit as st
import pandas as pd

st.title('machine learning app')

st.info('this is a machine learning app')
with st.expander('Data'):
  st.write('**asRaw data**')
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv")
  df

  st.write('**X**')
  X = df.drop('species', axis=1)
  X


  st.write('**y**')
  y = df.species
  y
              

  

