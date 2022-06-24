import streamlit as st
from welcome import welcome


options = [
    "Proyecto",
]

router = [
    welcome,
]


def callback():
    if "current" in st.session_state:
        del st.session_state[st.session_state.current]


def sidebar():
    with st.sidebar:
        opt = st.radio("", options, on_change=callback)

        idx = options.index(opt)

        return router[idx]
