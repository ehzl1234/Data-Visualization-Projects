import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_stock_data(symbol, period="1y"):
    """
    Get stock data for a given symbol
    
    Args:
        symbol (str): Stock symbol (e.g., 'AAPL', 'TSLA')
        period (str): Time period ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y')
    
    Returns:
        pandas.DataFrame: Stock data with Date, Open, High, Low, Close, Volume
    """
    try:
        # Create ticker object
        ticker = yf.Ticker(symbol)
        
        # Get historical data
        data = ticker.history(period=period)
        
        # Reset index to make Date a column
        data = data.reset_index()
        
        # Add symbol column
        data['Symbol'] = symbol
        
        return data
    
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def get_multiple_stocks(symbols, period="1y"):
    """
    Get stock data for multiple symbols
    
    Args:
        symbols (list): List of stock symbols
        period (str): Time period
    
    Returns:
        dict: Dictionary with symbol as key and DataFrame as value
    """
    stock_data = {}
    
    for symbol in symbols:
        print(f"Fetching data for {symbol}...")
        data = get_stock_data(symbol, period)
        if data is not None:
            stock_data[symbol] = data
    
    return stock_data

# List of popular stocks to analyze
DEFAULT_STOCKS = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']
