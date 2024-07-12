import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind, pearsonr
import numpy as np  # Import NumPy

def clean_and_merge_datasets(df1, df2):
    non_country_names = ["World", "Africa Eastern and Southern", "Africa Western and Central"]
    df1 = df1[~df1['country'].isin(non_country_names)].copy()
    df2 = df2[~df2['country'].isin(non_country_names)].copy()
    
    df1.loc[:, 'country'] = df1['country'].str.strip().str.lower()
    df2.loc[:, 'country'] = df2['country'].str.strip().str.lower()
    
    df2 = df2.rename(columns={'temperature_change': 'temperature'})
    
    matching_countries = set(df1['country']).intersection(set(df2['country']))
    df1 = df1[df1['country'].isin(matching_countries)].copy()
    df2 = df2[df2['country'].isin(matching_countries)].copy()
    
    df3 = pd.merge(df1, df2, on=['country', 'year'], how='inner')
    
    return df3

def add_columns_and_ensure_data_types(df3):
    industrial_countries = {'united states', 'canada', 'japan', 'germany', 'france', 'united kingdom', 'italy', 'australia', 'south korea'}
    global_north = {'united states', 'canada', 'japan', 'germany', 'france', 'united kingdom', 'italy', 'australia', 'new zealand', 'south korea', 'norway', 'sweden', 'denmark', 'finland', 'switzerland', 'austria', 'belgium', 'netherlands', 'luxembourg'}
    
    df3['industrial_level'] = df3['country'].apply(lambda x: 'industrial' if x in industrial_countries else 'no_industrial')
    df3['region'] = df3['country'].apply(lambda x: 'global north' if x in global_north else 'global south')
    
    df3['year'] = pd.to_numeric(df3['year'], errors='coerce')
    df3['population'] = pd.to_numeric(df3['population'], errors='coerce')
    df3['co2_emission'] = pd.to_numeric(df3['co2_emission'], errors='coerce')
    df3['temperature'] = pd.to_numeric(df3['temperature'], errors='coerce')
    
    return df3

def visualize_top_co2_emitters(df3):
    total_co2_emissions = df3.groupby('country')['co2_emission'].sum().reset_index()
    total_co2_emissions = total_co2_emissions.sort_values(by='co2_emission', ascending=False)
    top_20_emitters = total_co2_emissions.head(20)
    
    plt.figure(figsize=(14, 8))
    sns.barplot(x='co2_emission', y='country', data=top_20_emitters, palette='viridis')
    plt.title('Top 20 CO2 Emitters by Country (Sum of CO2 Emissions Over Years)')
    plt.xlabel('Total CO2 Emissions')
    plt.ylabel('Country')
    plt.show()
    
    return top_20_emitters

def visualize_top_temperature_changes(df3):
    total_temp_change = df3.groupby('country')['temperature'].sum().reset_index()
    total_temp_change = total_temp_change.sort_values(by='temperature', ascending=False)
    top_10_temp_change = total_temp_change.head(10)
    
    plt.figure(figsize=(14, 8))
    sns.barplot(x='temperature', y='country', data=top_10_temp_change, palette='coolwarm')
    plt.title('Top 10 Countries with Highest Temperature Change (Sum of Temperature Changes Over Years)')
    plt.xlabel('Total Temperature Change')
    plt.ylabel('Country')
    plt.show()
    
    return top_10_temp_change



import pandas as pd
import matplotlib.pyplot as plt


def calculate_and_visualize_co2_per_capita(df3):
    # Calculate CO2 emissions per capita
    df3['co2_per_capita'] = df3['co2_emission'] / df3['population']
    
    # Aggregate CO2 emissions per capita by year
    co2_per_capita_by_year = df3.groupby('year')['co2_per_capita'].mean().reset_index()
    
    # Display the CO2 emissions per capita by year
    print(co2_per_capita_by_year)
    
    # Visualization
    plt.figure(figsize=(12, 6))
    plt.plot(co2_per_capita_by_year['year'], co2_per_capita_by_year['co2_per_capita'], marker='o', linestyle='-')
    plt.title('CO2 Emissions Per Capita Over Years')
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions Per Capita')
    plt.grid(True)
    plt.show()

# Example usage:
# calculate_and_visualize_co2_per_capita(df3)





def hypothesis_test_temperature_change(df3):
    top_emitters_threshold = df3['co2_emission'].quantile(0.75)
    top_emitters = df3[df3['co2_emission'] >= top_emitters_threshold]
    non_top_emitters = df3[df3['co2_emission'] < top_emitters_threshold]
    
    t_stat, p_value = ttest_ind(top_emitters['temperature'], non_top_emitters['temperature'], equal_var=False)
    
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")
    
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='co2_emission', y='temperature', data=df3, showfliers=False)
    plt.axvline(x=top_emitters_threshold, color='red', linestyle='--', label='Top Emitters Threshold')
    plt.title('Temperature Change by CO2 Emissions')
    plt.xlabel('CO2 Emissions')
    plt.ylabel('Temperature Change')
    plt.legend()
    plt.show()
    
    avg_temp_top_emitters = top_emitters['temperature'].mean()
    avg_temp_non_top_emitters = non_top_emitters['temperature'].mean()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=['Top Emitters', 'Non-Top Emitters'], y=[avg_temp_top_emitters, avg_temp_non_top_emitters])
    plt.title('Average Temperature Change: Top Emitters vs Non-Top Emitters')
    plt.xlabel('Category')
    plt.ylabel('Average Temperature Change')
    plt.show()
    
    alpha = 0.05
    if p_value < alpha:
        print("The hypothesis is disproved: There is a statistically significant difference in temperature changes between top CO2 emitters and non-top emitters.")
    else:
        print("The hypothesis is not disproved: There is no statistically significant difference in temperature changes between top CO2 emitters and non-top emitters.")
    
    return t_stat, p_value



def analyze_correlation(df3):
    # Check for and handle infinite or NaN values
    df3 = df3.replace([np.inf, -np.inf], np.nan).dropna(subset=['co2_emission', 'temperature'])
    
    # Calculate the correlation coefficient between CO2 emissions and temperature changes
    correlation_coefficient, p_value = pearsonr(df3['co2_emission'], df3['temperature'])
    
    print(f"Correlation Coefficient: {correlation_coefficient}")
    print(f"P-value: {p_value}")
    
    alpha = 0.05
    if p_value < alpha:
        print("The hypothesis is supported: There is a statistically significant correlation between CO2 emissions and temperature changes.")
    else:
        print("The hypothesis is not supported: There is no statistically significant correlation between CO2 emissions and temperature changes.")
    
    # Visualization
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='co2_emission', y='temperature', data=df3)
    sns.regplot(x='co2_emission', y='temperature', data=df3, scatter=False, color='red')
    plt.title('Correlation Between CO2 Emissions and Temperature Changes')
    plt.xlabel('CO2 Emissions')
    plt.ylabel('Temperature Changes')
    plt.show()
    
    plt.figure(figsize=(10, 6))
    correlation_matrix = df3[['year', 'population', 'co2_emission', 'temperature']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix of Variables')
    plt.show()
    
    return correlation_coefficient, p_value

# Example usage:
# correlation_coefficient, p_value = fn.analyze_correlation(df3)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind



def analyze_development_status(df3):
    # Define lists of developed and developing countries (this is a basic list, adjust as needed)
    developed_countries = {'united states', 'canada', 'japan', 'germany', 'france', 'united kingdom', 'italy', 'australia', 'south korea'}
    developing_countries = set(df3['country']) - developed_countries

    # Add 'development_status' column
    df3['development_status'] = df3['country'].apply(lambda x: 'developed' if x in developed_countries else 'developing')

    # Hypothesis Testing
    # Aggregate CO2 emissions and temperature changes by development status
    co2_by_development_status = df3.groupby('development_status')['co2_emission'].mean()
    temp_by_development_status = df3.groupby('development_status')['temperature'].mean()

    # Perform t-test to compare temperature changes between developed and developing countries
    developed_temp = df3[df3['development_status'] == 'developed']['temperature']
    developing_temp = df3[df3['development_status'] == 'developing']['temperature']

    t_stat_temp, p_value_temp = ttest_ind(developed_temp, developing_temp, equal_var=False)

    # Perform t-test to compare CO2 emissions between developed and developing countries
    developed_co2 = df3[df3['development_status'] == 'developed']['co2_emission']
    developing_co2 = df3[df3['development_status'] == 'developing']['co2_emission']

    t_stat_co2, p_value_co2 = ttest_ind(developed_co2, developing_co2, equal_var=False)

    print(f"T-statistic (Temperature): {t_stat_temp}")
    print(f"P-value (Temperature): {p_value_temp}")
    print(f"T-statistic (CO2 Emissions): {t_stat_co2}")
    print(f"P-value (CO2 Emissions): {p_value_co2}")

    # Interpretation
    alpha = 0.05
    if p_value_temp < alpha:
        print("There is a statistically significant difference in temperature changes between developed and developing countries.")
    else:
        print("There is no statistically significant difference in temperature changes between developed and developing countries.")

    if p_value_co2 < alpha:
        print("There is a statistically significant difference in CO2 emissions between developed and developing countries.")
    else:
        print("There is no statistically significant difference in CO2 emissions between developed and developing countries.")

    # Visualization
    plt.figure(figsize=(12, 6))

    # Subplot 1: CO2 Emissions
    plt.subplot(1, 2, 1)
    sns.barplot(x=co2_by_development_status.index, y=co2_by_development_status.values)
    plt.title('Average CO2 Emissions by Development Status')
    plt.xlabel('Development Status')
    plt.ylabel('Average CO2 Emissions')

    # Subplot 2: Temperature Changes
    plt.subplot(1, 2, 2)
    sns.barplot(x=temp_by_development_status.index, y=temp_by_development_status.values)
    plt.title('Average Temperature Changes by Development Status')
    plt.xlabel('Development Status')
    plt.ylabel('Average Temperature Changes')

    plt.tight_layout()
    plt.show()

# Example usage:
# analyze_development_status(df3)

from scipy.stats import ttest_ind



def compare_co2_emissions_by_region(df3):
    # Aggregate CO2 emissions by region
    co2_by_region = df3.groupby('region')['co2_emission'].mean()
    
    # Perform t-test to compare CO2 emissions between Global North and Global South
    global_north_emissions = df3[df3['region'] == 'global north']['co2_emission']
    global_south_emissions = df3[df3['region'] == 'global south']['co2_emission']
    
    t_stat, p_value = ttest_ind(global_north_emissions, global_south_emissions, equal_var=False)
    
    print(f"T-statistic: {t_stat}")
    print(f"P-value: {p_value}")
    
    # Visualization
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='region', y='co2_emission', data=df3)
    plt.title('CO2 Emissions by Region')
    plt.xlabel('Region')
    plt.ylabel('CO2 Emissions')
    plt.show()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=co2_by_region.index, y=co2_by_region.values)
    plt.title('Average CO2 Emissions by Region')
    plt.xlabel('Region')
    plt.ylabel('Average CO2 Emissions')
    plt.show()

# Example usage:
# compare_co2_emissions_by_region(df3)





import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_trends_by_development_status(df3):
    # Aggregate CO2 emissions and temperature changes by year and development status
    co2_trend = df3.groupby(['year', 'development_status'])['co2_emission'].mean().reset_index()
    temp_trend = df3.groupby(['year', 'development_status'])['temperature'].mean().reset_index()

    # Visualization 1: CO2 Emissions Over Time
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=co2_trend, x='year', y='co2_emission', hue='development_status', marker='o')
    plt.title('CO2 Emissions Over Time by Development Status')
    plt.xlabel('Year')
    plt.ylabel('Average CO2 Emissions')
    plt.grid(True)
    plt.show()

    # Visualization 2: Temperature Changes Over Time
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=temp_trend, x='year', y='temperature', hue='development_status', marker='o')
    plt.title('Temperature Changes Over Time by Development Status')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature Changes')
    plt.grid(True)
    plt.show()

# Example usage:
# visualize_trends_by_development_status(df3)
