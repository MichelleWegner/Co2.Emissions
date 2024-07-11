import pandas as pd

#set the columns name to lower case, strip and replace empty spaces
def column_names(df_name):
    new_column_names = [column.strip().lower().replace(" ", "_") for column in df_name.columns]
    df_name.columns = new_column_names

#change the name of a column
def change_column_name(df, old_name, new_name):
    df.rename(columns={old_name: new_name}, inplace=True)
    return df 

#drop one column
def drop_column(df, column):
    df = df.drop(column,axis='columns')
    return df
#drop one row by the index
def drop_row_index(df, df_index):
    df = df.drop(index=df_index)
    return df
#change to numeric 
def to_numeric(df, columns_to_proces):
    for column in columns_to_proces: 
        df[column] = pd.to_numeric(df[column], errors='coerce')
