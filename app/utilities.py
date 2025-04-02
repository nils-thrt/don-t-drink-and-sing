
import streamlit  as st
from typing import Callable
from streamlit.delta_generator import DeltaGenerator
from streamlit import logger

from app.consts import BASE_DIR

def display_in_row( components : list[Callable[[DeltaGenerator], object]]):
    
    if (len(components) < 1):
        return
    
    columns = st.columns(len(components) + 2)
    
    returns = list()
    col_counter = 1

    for component in components:
        returns.append(component(columns[col_counter]))
        col_counter += 1

    return returns


def get_app_logger():
    return logger.get_logger("app")

def get_file_path(rel_path: str) :
    return f"{BASE_DIR}/{rel_path}"