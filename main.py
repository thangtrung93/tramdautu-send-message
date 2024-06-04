import streamlit as st
from streamlit.components.v1 import html
# from streamlit_telegram_login import telegram_login
from streamlit_telegram_login import TelegramLoginWidgetComponent
from streamlit_telegram_login.helpers import YamlConfig


bot_username = "@TramDauTuBot"
secret_key = "7135735816:AAFiOPeeK2mY9ygFibA5wr9NB_agG8g2AUg"

config = YamlConfig("main_config.yaml")
telegram_login = TelegramLoginWidgetComponent(**config.config)
st.write("## Example")
if not st.session_state["username"]:
    value = telegram_login.button
    if value:
        st.write(value)
else:
    st.write(telegram_login.get_session)

    clicked = st.button("Clear cookies")
    if clicked:
        telegram_login.clear_session()
        st.write("Cookies have been successfully cleared")