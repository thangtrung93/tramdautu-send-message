import streamlit as st
from streamlit.components.v1 import html
# from streamlit_telegram_login import telegram_login
from streamlit_telegram_login import TelegramLoginWidgetComponent


bot_username = "@TramDauTuBot"
secret_key = "7135735816:AAFiOPeeK2mY9ygFibA5wr9NB_agG8g2AUg"


telegram_login = TelegramLoginWidgetComponent(bot_username=bot_username, secret_key=secret_key)
value = telegram_login.button
st.write(value)