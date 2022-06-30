import streamlit as st
import pandas as pd
import numpy as np

from src.boolean.boolean_model import get_documents


def init_state():
    # required for preparing context switching
    st.session_state.current = "boolean_model"
    st.session_state.boolean_model = True
    ##########################################


def booleanmodel():
    st.title("Modelo Booleano")

    if not "boolean_model " in st.session_state:
        init_state()

    st.subheader("Introduzca la consulta")
    query = st.text_input("consulta")

    index, inverse_index = st.session_state.documents

    if query != "":
        result = get_documents(query, inverse_index, set(index.keys()))

        if len(result):
            df = pd.DataFrame(np.array(result), columns=["document"])

            st.dataframe(df)

        else:
            st.header("no existen resultados para esta consulta")

        # st.text_area(label="resultado", value=result)
