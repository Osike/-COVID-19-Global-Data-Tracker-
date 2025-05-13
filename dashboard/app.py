import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from helpers import load_data  # Shared function

# Page config
st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# Title
st.title("🌍 COVID-19 Global Dashboard")
st.markdown("Explore cases, deaths, and vaccinations by country.")

# Load data (cached)
@st.cache_data
def load_data():
    return pd.read_csv("../data/owid-covid-data.csv", parse_dates=['date'])

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries", 
    df['location'].unique(), 
    default=["United States", "India"]
)
metric = st.sidebar.selectbox(
    "Select Metric", 
    ["total_cases", "total_deaths", "people_vaccinated"]
)

# Filter data
filtered_df = df[df['location'].isin(selected_countries)]

# Main content
tab1, tab2 = st.tabs(["Trends", "Data"])

with tab1:
    # Line chart
    st.subheader(f"{metric.replace('_', ' ').title()} Over Time")
    st.line_chart(
        filtered_df.pivot(index="date", columns="location", values=metric),
        use_container_width=True
    )

with tab2:
    # Raw data
    st.subheader("Raw Data")
    st.dataframe(filtered_df.sort_values("date", ascending=False))

# Footer
st.markdown("Data source: [Our World in Data](https://github.com/owid/covid-19-data)")