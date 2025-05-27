import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from data_fetcher import get_multiple_stocks, DEFAULT_STOCKS

def create_price_chart(stock_data, symbols):
    """Create an interactive line chart showing stock prices"""
    fig = go.Figure()
    
    for symbol in symbols:
        if symbol in stock_data:
            data = stock_data[symbol]
            fig.add_trace(go.Scatter(
                x=data['Date'],
                y=data['Close'],
                mode='lines',
                name=symbol,
                line=dict(width=2)
            ))
    
    fig.update_layout(
        title="Stock Price Comparison",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        hovermode='x unified',
        template='plotly_white'
    )
    
    return fig

def create_volume_chart(stock_data, symbol):
    """Create a volume chart for a specific stock"""
    if symbol not in stock_data:
        return None
    
    data = stock_data[symbol]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=data['Date'],
        y=data['Volume'],
        name=f'{symbol} Volume',
        marker_color='lightblue'
    ))
    
    fig.update_layout(
        title=f"{symbol} Trading Volume",
        xaxis_title="Date",
        yaxis_title="Volume",
        template='plotly_white'
    )
    
    return fig

def calculate_moving_averages(data, window_short=20, window_long=50):
    """Calculate moving averages"""
    data = data.copy()
    data[f'MA_{window_short}'] = data['Close'].rolling(window=window_short).mean()
    data[f'MA_{window_long}'] = data['Close'].rolling(window=window_long).mean()
    return data

def create_ma_chart(stock_data, symbol):
    """Create a chart with moving averages"""
    if symbol not in stock_data:
        return None
    
    data = calculate_moving_averages(stock_data[symbol])
    
    fig = go.Figure()
    
    # Add closing price
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Close'],
        mode='lines',
        name=f'{symbol} Close',
        line=dict(color='blue')
    ))
    
    # Add moving averages
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['MA_20'],
        mode='lines',
        name='20-day MA',
        line=dict(color='orange', dash='dash')
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['MA_50'],
        mode='lines',
        name='50-day MA',
        line=dict(color='red', dash='dash')
    ))
    
    fig.update_layout(
        title=f"{symbol} - Price with Moving Averages",
        xaxis_title="Date",
        yaxis_title="Price ($)",
        template='plotly_white'
    )
    
    return fig

def main():
    """Main function to run the stock dashboard"""
    print("🚀 Starting Stock Market Dashboard...")
    print("=" * 50)
    
    # Get stock data
    print("📈 Fetching stock data...")
    stock_data = get_multiple_stocks(DEFAULT_STOCKS, period="6mo")
    
    if not stock_data:
        print("❌ No stock data retrieved!")
        return
    
    print(f"✅ Successfully retrieved data for: {list(stock_data.keys())}")
    
    # Create and show charts
    print("\n📊 Creating visualizations...")
    
    # 1. Price comparison chart
    price_fig = create_price_chart(stock_data, DEFAULT_STOCKS)
    price_fig.show()
    
    # 2. Volume chart for Apple
    volume_fig = create_volume_chart(stock_data, 'AAPL')
    if volume_fig:
        volume_fig.show()
    
    # 3. Moving averages for Tesla
    ma_fig = create_ma_chart(stock_data, 'TSLA')
    if ma_fig:
        ma_fig.show()
    
    print("\n🎉 Dashboard complete! Check your browser for interactive charts.")

if __name__ == "__main__":
    main()
