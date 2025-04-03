
import streamlit  as st
from typing import Callable
from utilities import *
from consts import BASE_DIR
from streamlit.delta_generator import DeltaGenerator
from streamlit import logger





st.title('A Random App')
st.write('Look at the pretty waves')

with open(f"{BASE_DIR}/app/css/all-page.css") as stylesheet:
    css = stylesheet.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.header("Don't drink and sing 🍹🎤", divider=True)




_, button_was_clicked = display_in_row([
    lambda col : col.image(f"{BASE_DIR}/images/spotify-icon-name/img-small.png"),
    lambda col : col.button("Login with Spotify")
])



if (button_was_clicked) :
    get_app_logger().info("Hat funktioniert!")


display_in_row([
    lambda col : col.button("Hello"),
])


get_app_logger().info("Hello")



