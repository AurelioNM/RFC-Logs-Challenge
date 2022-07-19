import streamlit as st

def nome():
    print("Hello World")

col1, col2, col3 = st.columns([1,1,1])
col2.button('Financial Transaction logs', on_click=nome)
col2.button('Financial Transaction logs', on_click=nome)
col2.button('Financial Transaction logs', on_click=nome)
