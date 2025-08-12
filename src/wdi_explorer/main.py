import seaborn as sns
import matplotlib.pyplot as plt
from data_fetcher import fetch_wdi_data

# Indicators: GDP per Capita, Life Expectancy
indicators = {
    "NY.GDP.PCAP.CD": "GDP per Capita",
    "SP.DYN.LE00.IN": "Life Expectancy"
}

df = fetch_wdi_data(indicators, countries=["USA", "CHN", "IND", "SGP"], start_year=2000)
df = df.reset_index().rename(columns={"country": "Country", "date": "Year"})

# GDP vs Life Expectancy (scatter)
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="GDP per Capita", y="Life Expectancy", hue="Country")
plt.title("GDP vs Life Expectancy")
plt.savefig("gdp_life_expectancy.png")
plt.close()
print("✅ gdp_life_expectancy.png saved.")

# Heatmap: Pivot table for Life Expectancy
pivot_df = df.pivot_table(values="Life Expectancy", index="Year", columns="Country")
plt.figure(figsize=(8,6))
sns.heatmap(pivot_df, cmap="YlGnBu")
plt.title("Life Expectancy Heatmap")
plt.savefig("education_heatmap.png")
plt.close()
print("✅ education_heatmap.png saved.")
