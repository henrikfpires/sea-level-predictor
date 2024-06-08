import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Original Data')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_predict = range(df['Year'].min(), 2051)
    y_predict = intercept + slope * x_predict
    plt.plot(x_predict, y_predict, 'r', label='Line of Best Fit')

    # Create second line of best fit (since year 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_predict_recent = range(df_recent['Year'].min(), 2051)
    y_predict_recent = intercept_recent + slope_recent * x_predict_recent
    plt.plot(x_predict_recent, y_predict_recent, 'g', label='Line of Best Fit (since 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.legend()
    plt.savefig('sea_level_plot.png')
    return plt.gca()