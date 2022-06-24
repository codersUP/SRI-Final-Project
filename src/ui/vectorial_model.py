import streamlit as st

from src.parse_query import create_index_query
from src.vectorial_model import calculate_rank


def init_state():
    # required for preparing context switching
    st.session_state.current = "vectorial_model"
    st.session_state.vectorial_model = True
    ##########################################


def vectorialmodel():
    st.title("Modelo Vectorial")

    if not "vectorial_model " in st.session_state:
        init_state()

    st.subheader("Introduzca la consulta")
    query = st.text_input("query")

    index, inverse_index = st.session_state.documents

    if query != "":
        query_index = create_index_query(query)

        result = calculate_rank(query_index, index, 3)

        st.text_area(label="resultado", value=result)
