#Imports
import pandas as pd
import streamlit as st

#====================Métricas====================

def apply_metric(dataframe: pd.DataFrame) -> None:

    #Variáveis
    vendas_totais = round(dataframe['Quantidade'].sum())
    valor_total = dataframe["Valor Total"].sum()
    valor_lucro = (dataframe["Valor Total"] - dataframe["Valor Pedido"]).sum()

    #Definição de Colunas de Métricas
    column_info0, column_info1, column_info2 = st.columns([1, 1, 1])
    with column_info0:
        st.metric(":shopping_trolley: Quantidade Total ", vendas_totais)
    with column_info1:
        st.metric(":moneybag: Valor Total", round(valor_total))
    with column_info2:
        st.metric(":money_mouth_face: Lucro Total", round(valor_lucro))

    return