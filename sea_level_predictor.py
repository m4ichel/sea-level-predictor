import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    ### Read data from file

    # transfer the csv data do the df variable in a pd.DataFrame format
    df = pd.read_csv("epa-sea-level.csv")

    ### Create scatter plot

    # define the x and y values
    original_x = df["Year"]
    original_y = df["CSIRO Adjusted Sea Level"]
    # plot the scatter plot
    plt.scatter(original_x, original_y)

    ### Create first line of best fit

    # here we get the slope and intercept from the linear regressor (m and b from the equation of a line)
    slope, intercept, _, _, _ = linregress(original_x, original_y)
    # then we extend the x axis to include all years in the data and more up until 2050 (does not include 2051)
    extended_x = np.arange(int(original_x.min()), 2051)
    # and finally calculate the line using the formula mx + b
    extended_y = slope * extended_x + intercept
    # then we plot the line with the color red
    plt.plot(extended_x, extended_y, 'r')

    ### Create second line of best fit

    # select only the x and y values after (or at) the year 2000 for the linear regression
    recent_x = df[df["Year"] >= 2000]["Year"]
    recent_y = df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"]
    # get the recent slope and intercept from the linear regressor
    slope_recent, intercept_recent, _, _, _ = linregress(recent_x, recent_y)
    # calculate the line using the formula
    extended2000_y = slope_recent * extended_x + intercept_recent
    # then we plot the line with the color green
    plt.plot(extended_x, extended2000_y, 'g')

    ### Add labels and title
    
    # add x and y labels
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    # add title
    plt.title("Rise in Sea Level")
    
    ### Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()