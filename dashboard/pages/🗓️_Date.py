import streamlit as st
import pandas as pd


if 'df' not in st.session_state:
    df = pd.read_csv('clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']


st.header("Date")
st.write("The bar chart below represents the distribution of number of twittes with MahsaAmini hashtag in each date")
st.subheader("Number of twiites with MahsaAmini hashtag")

genre = st.radio(
    "What's your favorite movie genre",
    ('Twitte', 'User'))

if genre == 'Twitte':
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['date'] = df['created_at'].dt.date

    dates = df['date'].value_counts()
    st.line_chart(data=dates)
else:
    df['user/created_at'] = pd.to_datetime(df['user/created_at'])
    df['user/year'] = df['user/created_at'].dt.year



    users_date = df.groupby(by='user/year')['user_id'].count()
    users_date = users_date.reset_index()
    users_date['user/year'] = users_date['user/year'].astype("str")
    st.line_chart(data=users_date, x='user/year', y='user_id')

    st.metric("Amount of people sign up to twiter after increase amount of tweets with Mahsa Amini hashtag","17.3%")
