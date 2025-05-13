import pandas as pd

def load_data():
    """Load and cache the COVID-19 dataset."""
    return pd.read_csv("../data/owid-covid-data.csv", parse_dates=['date'])

def clean_data(df):
    """Clean the dataset (shared between notebook and dashboard)."""
    df = df[df['location'].isin(["United States", "India", "Kenya"])]
    df['total_cases'] = df['total_cases'].fillna(0)
    return df
