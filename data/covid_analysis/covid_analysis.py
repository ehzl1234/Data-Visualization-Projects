import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import requests
from datetime import datetime

def fetch_covid_data():
    """
    Fetch COVID-19 data from a reliable API source
    Returns: DataFrame with COVID data by country
    """
    try:
        # Using disease.sh API for reliable COVID data
        url = "https://disease.sh/v3/covid-19/countries"
        response = requests.get(url)
        data = response.json()
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Select relevant columns
        columns_to_keep = [
            'country', 'cases', 'todayCases', 'deaths', 'todayDeaths',
            'recovered', 'active', 'casesPerOneMillion', 'deathsPerOneMillion',
            'population', 'continent'
        ]
        
        df = df[columns_to_keep]
        return df
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def create_top_countries_chart(df, metric='cases', top_n=15):
    """Create a bar chart showing top countries by specified metric"""
    
    # Sort and get top countries
    top_countries = df.nlargest(top_n, metric)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=top_countries['country'],
        y=top_countries[metric],
        marker_color='crimson',
        text=top_countries[metric],
        textposition='auto',
    ))
    
    fig.update_layout(
        title=f"Top {top_n} Countries by {metric.title()}",
        xaxis_title="Country",
        yaxis_title=metric.title(),
        template='plotly_white',
        xaxis_tickangle=-45
    )
    
    return fig

def create_continent_comparison(df):
    """Create a comparison chart by continent"""
    
    # Group by continent
    continent_data = df.groupby('continent').agg({
        'cases': 'sum',
        'deaths': 'sum',
        'recovered': 'sum',
        'population': 'sum'
    }).reset_index()
    
    # Calculate rates per million
    continent_data['cases_per_million'] = (continent_data['cases'] / continent_data['population']) * 1000000
    continent_data['deaths_per_million'] = (continent_data['deaths'] / continent_data['population']) * 1000000
    
    fig = go.Figure()
    
    # Add cases per million
    fig.add_trace(go.Bar(
        name='Cases per Million',
        x=continent_data['continent'],
        y=continent_data['cases_per_million'],
        marker_color='lightblue'
    ))
    
    # Add deaths per million
    fig.add_trace(go.Bar(
        name='Deaths per Million',
        x=continent_data['continent'],
        y=continent_data['deaths_per_million'],
        marker_color='darkred'
    ))
    
    fig.update_layout(
        title="COVID-19 Impact by Continent (Per Million Population)",
        xaxis_title="Continent",
        yaxis_title="Rate per Million",
        barmode='group',
        template='plotly_white'
    )
    
    return fig

def create_scatter_analysis(df):
    """Create scatter plot analyzing relationship between population and cases"""
    
    # Filter out countries with very small populations for clearer visualization
    df_filtered = df[df['population'] > 1000000].copy()
    
    fig = px.scatter(
        df_filtered,
        x='population',
        y='cases',
        size='deaths',
        color='continent',
        hover_name='country',
        hover_data=['casesPerOneMillion', 'deathsPerOneMillion'],
        title="COVID Cases vs Population by Country",
        labels={
            'population': 'Population',
            'cases': 'Total Cases',
            'deaths': 'Deaths (size of bubble)'
        }
    )
    
    fig.update_layout(
        template='plotly_white',
        xaxis_type="log",
        yaxis_type="log"
    )
    
    return fig

def generate_summary_stats(df):
    """Generate summary statistics"""
    
    total_cases = df['cases'].sum()
    total_deaths = df['deaths'].sum()
    total_recovered = df['recovered'].sum()
    countries_affected = len(df[df['cases'] > 0])
    
    print("🌍 GLOBAL COVID-19 SUMMARY")
    print("=" * 40)
    print(f"📊 Total Cases: {total_cases:,}")
    print(f"💀 Total Deaths: {total_deaths:,}")
    print(f"💚 Total Recovered: {total_recovered:,}")
    print(f"🌎 Countries Affected: {countries_affected}")
    print(f"📈 Global Death Rate: {(total_deaths/total_cases)*100:.2f}%")
    print("=" * 40)

def main():
    """Main function to run the COVID analysis"""
    
    print("🦠 COVID-19 Global Data Analysis")
    print("=" * 50)
    
    # Fetch data
    print("📥 Fetching latest COVID-19 data...")
    df = fetch_covid_data()
    
    if df is None:
        print("❌ Failed to fetch data!")
        return
    
    print(f"✅ Data fetched successfully! Analyzing {len(df)} countries...")
    
    # Generate summary
    generate_summary_stats(df)
    
    # Create visualizations
    print("\n📊 Creating visualizations...")
    
    # 1. Top countries by cases
    cases_chart = create_top_countries_chart(df, 'cases', 15)
    cases_chart.show()
    
    # 2. Top countries by deaths
    deaths_chart = create_top_countries_chart(df, 'deaths', 15)
    deaths_chart.show()
    
    # 3. Continent comparison
    continent_chart = create_continent_comparison(df)
    continent_chart.show()
    
    # 4. Scatter analysis
    scatter_chart = create_scatter_analysis(df)
    scatter_chart.show()
    
    print("\n🎉 Analysis complete! Check your browser for interactive charts.")
    print(f"📅 Data last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Run the analysis
main()
