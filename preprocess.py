import pandas as pd

def preprocess_data(df):
    df = df.select_dtypes(include=["number"])
    df = df.fillna(0)
    return df
print("Preprocessing started...")
print("Preprocessing completed.")