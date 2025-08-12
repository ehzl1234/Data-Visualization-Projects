import pandas as pd

def load_happiness_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

if __name__ == "__main__":
    df = load_happiness_data("world-happiness-report-2024.csv")
    print(df.head())
