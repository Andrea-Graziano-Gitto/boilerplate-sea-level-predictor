import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit
    result = linregress(df['Year'],  df['CSIRO Adjusted Sea Level'])

    # Create second line of best fit
    
    # Extend the line of best fit to 2050
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, result.intercept + result.slope * years_extended, color='green', label='Best Fit Line 2')
    # Create second line of best fit for data from 2000 onwards
    df_2000 = df[df['Year'] >= 2000]
    result_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
   
    # Extend the second line of best fit to 2050
    years_extended_2000 = pd.Series(range(2000, 2051))
    plt.plot(years_extended_2000, result_2000.intercept + result_2000.slope * years_extended_2000, color='purple', label='Best Fit Line 4')

    # Add labels and title

    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()