import streamlit as st
import pandas as pd


st.set_page_config(page_title="Verified Accounts", 
                    page_icon="✅")

if 'sorted_verifide_account' not in st.session_state:
    sorted_verifide_account = pd.read_csv('data\\new_verified_account.csv')
    st.session_state['sorted_verifide_account'] = sorted_verifide_account
else:
    sorted_verifide_account = st.session_state['sorted_verifide_account']


st.header("Verified Accounts")
st.write("The bar chart below represents the distribution of number of verified accounts which twitte with MahsaAmini hashtag")
st.subheader("Number of verifide accounts and ordinary accounts")


sorted_verifide_account = sorted_verifide_account.reset_index()
sorted_verifide_account.rename(columns={'index': 'Verified'}, inplace=True)


st.bar_chart(sorted_verifide_account, x='Verified', y='user_verified')
