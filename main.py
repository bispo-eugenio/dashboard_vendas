#imports
import streamlit as st
from data.load_data import load_data
from componets.filter import apply_sidebar_filsters
from utils.constants import PATH_IMG_ICON
from componets.metric import apply_metric
from componets.graph import bar_graph, line_graph, arc_graph

#====================Configurações da Página====================
st.set_page_config(
    page_title="DASHBOARD",
    page_icon=f"{PATH_IMG_ICON}",
    layout="wide",
    initial_sidebar_state="auto",
)

#====================Principal====================
def main() -> None:

    #Configurações
    df = load_data("data\\system_extraction.xlsx")
    st.title(":bar_chart: Dashboard de Vendas")
    df_filtered = apply_sidebar_filsters(df)

    #Definição de Colunas
    column0, column1 = st.columns([3.5,4.5])
    column2, column3 = st.columns([3.5, 4.5])
    column4, column5 = st.columns([3.5,4.5])

    #Organização de Layout
    with column0:
        bar_graph(df_filtered, "Cliente", "Valor Pedido")
    with column1:
        line_graph(df_filtered, "Região", "Margem Lucro")
    with column2:
        arc_graph(df_filtered, "Vendedor", "Quantidade")
    with column3:
        arc_graph(df_filtered, "Região", "Quantidade")
    with column4:
        bar_graph(df_filtered, "Vendedor", "Valor Pedido")
    with column5:
        line_graph(df_filtered, "Data", "Valor Total")

    #Aplicando Métrica
    apply_metric(df_filtered)

    return

if __name__ == "__main__":
    main()