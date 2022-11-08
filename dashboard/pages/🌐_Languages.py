import streamlit as st
import pandas as pd


if 'df' not in st.session_state:
    df = pd.read_csv('clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']


st.header("Languages")
st.write("Number of twittes with each languages")
st.subheader("Number of twittes by language")


lang=df['lang'].value_counts()
st.bar_chart(lang)