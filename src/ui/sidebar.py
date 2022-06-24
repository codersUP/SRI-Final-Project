import streamlit as st
from src.utils import load_index_and_inverse_index
from src.ui.welcome import welcome
from src.ui.vectorial_model import vectorialmodel
from src.ui.boolean_model import booleanmodel


options = ["Proyecto", "Modelo Vectorial", "Modelo Booleano"]

router = [welcome, vectorialmodel, booleanmodel]


def callback():
    # TODO calculate results when not exists
    if "documents" not in st.session_state:
        index, inverse_index = load_index_and_inverse_index("results.json")
        st.session_state.documents = (index, inverse_index)

    if "current" in st.session_state and st.session_state.current in st.session_state:
        del st.session_state[st.session_state.current]


def sidebar():
    with st.sidebar:
        st.header("¿Cuál modelo desea usar?")
        opt = st.radio("", options, on_change=callback)

        idx = options.index(opt)

        return router[idx]
