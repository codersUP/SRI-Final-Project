import streamlit as st
from src.constants import A
from src.vectorial.parse_query import create_index_query
from src.vectorial.vectorial_model import calculate_rank
import pandas as pd
import numpy as np

from src.utils import filter_rank_value_greater_0
from src.vectorial.expand_query import expand_query, replace_expand_in_query


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
    query = st.text_input("consulta")

    index, inverse_index = st.session_state.documents

    if query != "":
        query_index = create_index_query(query, A, inverse_index)

        result = calculate_rank(query_index, index, 10)
        filtered_result = filter_rank_value_greater_0(result)

        if len(filtered_result):
            df = pd.DataFrame(np.array(filtered_result), columns=["value", "document"])

            st.dataframe(df)

        else:
            st.header("no existen resultados para esta consulta")

        expanded = expand_query(query_index, inverse_index)
        if len(expanded):
            st.header("quizás quiso decir:")

            expanded_query = replace_expand_in_query(query, expanded)
            st.text(expanded_query)
