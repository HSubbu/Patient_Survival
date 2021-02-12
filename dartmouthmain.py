#mainapp.py
import page1
import page2
import page3
import mainpage
import streamlit as st
PAGES = {
    "Home Page":mainpage,
    "Features":page3,
    "Plots": page1,    
    "Model Prediction": page2,
    
}
st.sidebar.title('Navigation ')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()