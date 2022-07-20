import streamlit as st
from helper import generateUser
from logger import logger


def routesInfo():
    user = generateUser()
    logger.info('User %s successfully registered e-mail %s@domain.com' % (user, user))
    



col1, col2, col3 = st.columns([1,1,1])
st.button('Routes Logs', on_click=routesInfo)
# col2.button('Webhook Logs', on_click=nome)
# col2.button('User Registration Logs', on_click=nome)
# col2.button('Financial Transaction Logs', on_click=nome)