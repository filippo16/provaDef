import pandas as pd

def create_df(name_path):
    df = pd.read_csv(name_path, sep=';')

    df['Mv'] = df['Mv'].str.replace(",", ".")
    df['Fm'] = df['Fm'].str.replace(",", ".")
    df['Mv'] = df['Mv'].astype(float)
    df['Fm'] = df['Fm'].astype(float)
    return df
