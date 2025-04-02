
import streamlit  as st
from typing import Callable
from utilities import *
from consts import BASE_DIR
from streamlit.delta_generator import DeltaGenerator
from streamlit import logger


css = open(f"{BASE_DIR}/app/css/all-page.css").readlines()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)



st.header("Don't drink and sing 🍹🎤", divider=True)


def on_spotify_login() :
    st.text("Du hast den Button geklickt")

display_in_row([
    lambda col : col.image(f"{BASE_DIR}/images/spotify-icon-name/img-small.png"),
    lambda col : col.button("Login with Spotify", on_click=on_spotify_login)
])


display_in_row([
    lambda col : col.button("Hello"),
])


get_app_logger().info("Hello")



