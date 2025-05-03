import pandas as pd
import streamlit as st
import altair as alt
from utils.constants import PRIMARY_COLOR, SECONDARY_COLOR


#====================Gráficos====================

#Gráfico de Barra
def bar_graph(dataframe: pd.DataFrame, set_x: str | None = None, set_y:str |
        None = None, title: str = "", color_bar = PRIMARY_COLOR) -> None:
    try:
        st.subheader(title)

        chart_bar = dataframe.groupby(set_x)[set_y].mean().reset_index()
        chart_bar.columns = [set_x, set_y]
        bar = st.bar_chart(
            chart_bar,
            x=set_x, y= set_y,
            color=[color_bar]
        )
        return bar

    except KeyError as e:
        raise KeyError(f"Erro ao acessar coluna no DataFrame: {e}")
    except ValueError as e:
        raise ValueError(f"Erro de valor: {e}")
    except Exception as e:
        raise RuntimeError(f"Erro ao criar {e}")

#Gráfico de Linha
def line_graph(dataframe: pd.DataFrame, nominal: str | None = None, quantitative_one: str |
        None = None, quantitative_two: str | None = None, title: str = "") -> None:
    try:
        if quantitative_two is not None:
            st.subheader(title)

            chart_table = dataframe.groupby(nominal, as_index=False).agg({
                quantitative_one: "mean",
                quantitative_two: "mean"
            })
            chart_table.columns = [nominal, quantitative_one, quantitative_two]
            line = st.line_chart(
                chart_table,
                x=nominal, y=[quantitative_one, quantitative_two],
                color=[PRIMARY_COLOR, SECONDARY_COLOR],
            )
            return line
        else:
            st.subheader(title)

            chart_table = dataframe.groupby(nominal, as_index=False).agg({
                quantitative_one: lambda x: round(x.mean()),
            })
            chart_table.columns = [nominal, quantitative_one]
            line = st.line_chart(
                chart_table,
                x=nominal, y=quantitative_one,
                color=PRIMARY_COLOR
            )
            return line

    except KeyError as e:
        raise KeyError(f"Erro ao acessar coluna no DataFrame: {e}")
    except ValueError as e:
        raise ValueError(f"Erro de valor: {e}")
    except Exception as e:
        raise RuntimeError(f"Erro ao criar {e}")

#Gráfico de Pizza
def arc_graph(dataframe: pd.DataFrame, nominal: str | None = None, quantitative: str |
        None = None, title: str = "", radius: int = 100) -> None:
    try:
        st.subheader(title)

        chart_table = dataframe.groupby(nominal, as_index=False).agg({
            quantitative: "sum"
        })
        chart_arc = (
            alt.Chart(chart_table).mark_arc(innerRadius=radius).encode(
            color= alt.Color(field=nominal, type="nominal"),
            theta= alt.Theta(field=quantitative, type="quantitative")
            )
        )
        return st.altair_chart(chart_arc)

    except KeyError as e:
        raise KeyError(f"Erro ao acessar coluna no DataFrame: {e}")
    except ValueError as e:
        raise ValueError(f"Erro de valor: {e}")
    except Exception as e:
        raise RuntimeError(f"Erro ao criar {e}")