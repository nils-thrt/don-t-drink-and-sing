
import streamlit  as st
from typing import Callable
from streamlit.delta_generator import DeltaGenerator
from streamlit import logger

def display_in_row( components : list[Callable[[DeltaGenerator], None]]):
    
    if (len(components) < 1):
        return
    
    columns = st.columns(len(components) + 2    )

    counter = 1
    for component in components:
        component(columns[counter])
        counter += 1


def get_app_logger():
    return logger.get_logger("app")