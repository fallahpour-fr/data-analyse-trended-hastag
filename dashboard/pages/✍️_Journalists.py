import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


if 'journalist' not in st.session_state:
    journalist = pd.read_csv('data\journalist.csv')
    st.session_state['journalist'] = journalist
else:
    journalist = st.session_state['journalist']


st.header("Type of people")
st.write("The bar chart below represents the distribution of number of people with MahsaAmini hashtag in each date")
st.subheader("Number of type of people with MahsaAmini hashtag")

type = st.selectbox(
    "What's your favorite movie genre",
    ('Journalist', 'Other'))


if type=='Other':
    st.line_chart(data =journalist, x='time', y='other')
else:
    st.line_chart(data =journalist, x='time', y='Journalist')

fig, ax = plt.subplots()
ax.pie([journalist['Journalist'].sum(), journalist['other'].sum()], 
        labels=['Journalist', 'other'],
        explode = [0, 0.2],
        autopct='%1.1f%%')

st.pyplot(fig)

