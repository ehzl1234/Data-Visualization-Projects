import pandas as pd
import plotly.express as px
from data_fetcher import load_happiness_data

# Download dataset if not present
DATA_FILE = "world-happiness-report-2024.csv"
try:
    df = load_happiness_data(DATA_FILE)
except FileNotFoundError:
    print(f"Dataset {DATA_FILE} not found. Download it from Kaggle and place in this folder.")
    exit()

# Scatter plot: Happiness Score vs GDP per capita
fig_scatter = px.scatter(
    df,
    x="GDP per capita",
    y="Happiness score",
    color="Region",
    hover_name="Country",
    title="Happiness vs GDP per capita"
)
fig_scatter.write_image("factor_scatter.png")
print("✅ factor_scatter.png saved.")

# Choropleth Map
fig_map = px.choropleth(
    df,
    locations="Country",
    locationmode="country names",
    color="Happiness score",
    title="World Happiness Map",
    color_continuous_scale="Viridis"
)
fig_map.write_image("happiness_map.png")
print("✅ happiness_map.png saved.")
