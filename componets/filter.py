#Imports
import pandas as pd
import streamlit as st

#====================Filtros====================

def apply_sidebar_filsters(dataframe: pd.DataFrame) -> pd.DataFrame:

    #SideBar para Filtragem
    with st.sidebar:

        #Variáveis
        min_date = dataframe["Data"].min().to_pydatetime()
        max_date = dataframe["Data"].max().to_pydatetime()

        #Título
        st.header("Filtro")

        #Filtragem de Região
        filter_country = st.selectbox(
            "Região",
            options = dataframe["Região"].unique(),
            index = None,
            placeholder= "Opções"
        )

        #Filtragem de Vendedor
        filter_salesman = st.selectbox(  # -> Seleciona Vendedor
            "Vendedor",
            options=dataframe["Vendedor"].unique(),
            index=None,
            placeholder="Opções",
        )

        #Filtragem de Cliente
        filter_client = st.selectbox(
            "Cliente",
            options = dataframe["Cliente"].unique(),
            index = None,
            placeholder = "Opções"
        )

        #Filtragem de Produto
        filter_product = st.multiselect(
            "Produto",
            options = sorted(dataframe["Produto vendido"].unique()),
            placeholder = "Opções"
        )

        #Filtragem de Data
        filter_date = st.slider(
            "Data",
            min_value = min_date,
            max_value = max_date,
            value = (min_date, max_date)
        )

    #Lógica de Aplicação de Filtragem
    if filter_country:
        dataframe = dataframe[dataframe['Região'] == filter_country]
    if filter_salesman:
        dataframe = dataframe[dataframe['Vendedor'] == filter_salesman]
    if filter_client:
        dataframe = dataframe[dataframe["Cliente"] == filter_client]
    if filter_product:
        dataframe = dataframe[dataframe['Produto vendido'].isin(filter_product)]
    if filter_date:
        dataframe = dataframe[(dataframe['Data'] >= filter_date[0]) & (dataframe['Data'] <= filter_date[1])]

    return dataframe