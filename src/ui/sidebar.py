import json
import streamlit as st
from src.parse_document import create_index
from src.parse_directory import get_files_from_path_list
from src.utils import load_index_and_inverse_index, save_index_and_inverse_index
from src.ui.welcome import welcome
from src.ui.vectorial_model import vectorialmodel
from src.ui.boolean_model import booleanmodel
import os.path


options = ["Proyecto", "Modelo Vectorial", "Modelo Booleano"]

router = [welcome, vectorialmodel, booleanmodel]


def callback():
    if not os.path.isfile("results.json"):
        f = open("files_path.json")
        json_files_path = json.load(f)

        files = get_files_from_path_list(json_files_path["paths"])
        index, inverse_index = create_index(files, verbose=True)

        save_index_and_inverse_index(
            "results.json", index=index, inverse_index=inverse_index
        )

        if "documents" in st.session_state:
            del st.session_state["documents"]

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
