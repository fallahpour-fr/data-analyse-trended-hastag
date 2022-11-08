import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




if 'gender' not in st.session_state:
    gender = pd.read_csv('data\gender.csv')
    st.session_state['gender'] = gender
else:
    gender = st.session_state['gender']



st.header("Gender")
st.write("The bar chart below represents the distribution of number of men and female who twiite with MahsaAmini hashtag as journalist or ordinary people")
st.subheader("Number of men and women")


genders = gender.value_counts()
genders = genders.reset_index(name='Count')
st.bar_chart(genders, x='gender', y='Count')

