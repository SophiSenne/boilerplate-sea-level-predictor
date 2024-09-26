import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Sea Level Data')
    plt.grid(True)

    # Create first line of best fit for entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(1880, 2051)
    sea_levels_predicted = slope * years_extended + intercept
    plt.plot(years_extended, sea_levels_predicted, color='r', label='Best Fit Line (Prediction)')

    # Filter data from year 2000 onwards for second line of best fit
    recent_data = df[df['Year'] >= 2000]
    
    # Create second line of best fit using data from 2000 onwards
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_extended_recent = np.arange(2000, 2051)
    sea_levels_predicted_recent = slope_recent * years_extended_recent + intercept_recent
    plt.plot(years_extended_recent, sea_levels_predicted_recent, color='g', label='Best Fit Line (2000 Onwards)')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    plt.tight_layout()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
