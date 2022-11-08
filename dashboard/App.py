import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Start",
    page_icon="👋",
)

if 'df' not in st.session_state:
    df = pd.read_csv('data/clean_dataset.csv')
    st.session_state['df'] = df
else:
    df = st.session_state['df']

if 'sorted_verifide_account' not in st.session_state:
    sorted_verifide_account = pd.read_csv('data\\new_verifide_account.csv')
    st.session_state['sorted_verifide_account'] = sorted_verifide_account
else:
    sorted_verifide_account = st.session_state['sorted_verifide_account']

if 'mask' not in st.session_state:
    mask = pd.read_csv('data\mask.csv')
    st.session_state['mask'] = mask
else:
    mask = st.session_state['mask']

if 'gender' not in st.session_state:
    gender = pd.read_csv('data\gender.csv')
    st.session_state['gender'] = gender
else:
    gender = st.session_state['gender']

if 'journalist' not in st.session_state:
    journalist = pd.read_csv('data\journalist.csv')
    st.session_state['journalist'] = journalist
else:
    journalist = st.session_state['journalist']


st.header("This is start page! 👋")
st.write("Write a cool description here")
st.markdown("""
            **Professor's name**

            **Created By Anna**
            
            """)




# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )