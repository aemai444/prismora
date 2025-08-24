import streamlit as st
from page_definition2 import main_page

# set up the page
st.set_page_config(page_title="SupportCircle")

options = ["Mainpage", "Contacts", "Checkbox", "Information", "Your AI assistant", "FAQ"]
page_selection = st.sidebar.selectbox("Menu", options)


if page_selection == "Mainpage":
    main_page()