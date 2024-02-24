import streamlit as st
import langchain_helper


st.title("Restaurant Menu Generator")

cuisine = st.sidebar.selectbox("pick a cuisine", ("indian", "italian", "chinese", "mexican", "arabian"))

if cuisine:
    response = langchain_helper.generate_name_and_items(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response['items'].strip().split(",")
    st.write("-----------------------------------MENU ITEMS-----------------------------------")
    for item in menu_items:
        st.write("-", item)


