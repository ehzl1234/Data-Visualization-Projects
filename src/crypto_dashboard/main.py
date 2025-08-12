import plotly.graph_objects as go
<<<<<<< HEAD
import pandas as pd
from data_fetcher import fetch_crypto_data

# List of cryptos to compare
cryptos = ["bitcoin", "ethereum", "dogecoin"]

# --- Bitcoin Single Chart ---
print("\n📊 Fetching Bitcoin data...")
btc_df = fetch_crypto_data("bitcoin", days=90)

if btc_df.empty:
    print("⚠ No Bitcoin data retrieved, skipping btc_chart.png")
else:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=btc_df["timestamp"], y=btc_df["price"], mode="lines", name="BTC Price"))
    fig.update_layout(title="Bitcoin Price (Last 90 days)", xaxis_title="Date", yaxis_title="Price (USD)")
    fig.write_image("btc_chart.png")
    print("✅ btc_chart.png saved.")

# --- Multi-Crypto Comparison ---
multi_df = pd.DataFrame()

print("\n📊 Fetching multi-crypto data...")
for coin in cryptos:
    temp_df = fetch_crypto_data(coin, days=30)
    if temp_df.empty:
        print(f"⚠ No data for {coin}, skipping.")
        continue
=======
from data_fetcher import fetch_crypto_data
import pandas as pd

# Fetch BTC data for last 90 days
df = fetch_crypto_data("bitcoin", days=90)

# Line chart for BTC price
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["timestamp"], y=df["price"], mode="lines", name="BTC Price"))
fig.update_layout(title="Bitcoin Price (Last 90 days)", xaxis_title="Date", yaxis_title="Price (USD)")
fig.write_image("btc_chart.png")
print("✅ btc_chart.png saved.")

# Example for multiple cryptos
cryptos = ["bitcoin", "ethereum", "dogecoin"]
multi_df = pd.DataFrame()
for coin in cryptos:
    temp_df = fetch_crypto_data(coin, days=30)
>>>>>>> 9766fc19ab65a996af2a6a861b6a0f24e4083a44
    temp_df.rename(columns={"price": coin}, inplace=True)
    if multi_df.empty:
        multi_df = temp_df
    else:
<<<<<<< HEAD
        multi_df = pd.merge(multi_df, temp_df, on="timestamp", how="outer")

# Plot multi-crypto chart if data exists
if not multi_df.empty:
    fig_multi = go.Figure()
    for coin in cryptos:
        if coin not in multi_df.columns:
            print(f"⚠ {coin} column missing, skipping plot line.")
            continue
        fig_multi.add_trace(go.Scatter(
            x=multi_df["timestamp"], 
            y=multi_df[coin], 
            mode="lines", 
            name=coin.capitalize()
        ))
    fig_multi.update_layout(title="Crypto Price Comparison (30 days)", xaxis_title="Date", yaxis_title="Price (USD)")
    fig_multi.write_image("crypto_comparison.png")
    print("✅ crypto_comparison.png saved.")
else:
    print("⚠ No crypto data available for comparison chart.")
=======
        multi_df = pd.merge(multi_df, temp_df, on="timestamp")

fig_multi = go.Figure()
for coin in cryptos:
    fig_multi.add_trace(go.Scatter(x=multi_df["timestamp"], y=multi_df[coin], mode="lines", name=coin.capitalize()))
fig_multi.update_layout(title="Crypto Price Comparison (30 days)", xaxis_title="Date", yaxis_title="Price (USD)")
fig_multi.write_image("crypto_comparison.png")
print("✅ crypto_comparison.png saved.")
>>>>>>> 9766fc19ab65a996af2a6a861b6a0f24e4083a44
