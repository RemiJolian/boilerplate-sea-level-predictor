import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    file_path = (
           "D:\\1-Programming\\1-Training_Files & Codes\\Python\\1-Ramin's Codes\\Data_Analysis\\"
            "5 Projects\\boilerplate-sea-level-predictor\\epa-see-level.csv")

    df = pd.read_csv(file_path)

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'] )
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')

    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()