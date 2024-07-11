import pandas as pd

def column_names(df_name):
    new_column_names = [column.strip().lower().replace(" ", "_") for column in df_name.columns]
    df_name.columns = new_column_names