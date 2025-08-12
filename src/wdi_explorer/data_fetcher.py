import pandas as pd
import wbdata
import datetime

def fetch_wdi_data(indicators, countries=["USA", "CHN", "IND"], start_year=2000):
    start = datetime.datetime(start_year, 1, 1)
    df = wbdata.get_dataframe(indicators, country=countries, data_date=(start, datetime.datetime.now()))
    return df

if __name__ == "__main__":
    indicators = {"NY.GDP.PCAP.CD": "GDP per Capita", "SP.DYN.LE00.IN": "Life Expectancy"}
    df = fetch_wdi_data(indicators)
    print(df.head())
