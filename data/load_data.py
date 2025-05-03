#Imports
import pandas as pd

#====================Cria DataFrame====================
def load_data(dataframe: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(dataframe)
        df_copy = df.copy()
        df_copy["Margem Lucro"] = df_copy["Margem Lucro"] = round(df_copy["Margem Lucro"], 2)
        df_copy['Valor Total'] = round(
            df_copy["Valor Pedido"] + (df_copy["Valor Pedido"] * (df_copy["Margem Lucro"] / 100)), 2)
        df_copy["Data"] = pd.to_datetime(df_copy["Data"])
    except Exception as e:
        raise RuntimeError(f"Erro ao carragar o DataFrame: {e}")

    return df_copy
