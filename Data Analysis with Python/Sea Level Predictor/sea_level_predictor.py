import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  
  # Create scatter plot
  df.plot(x = "Year",y = 'CSIRO Adjusted Sea Level', label='original data', kind = "scatter", figsize = (10,10))
  
  # Create first line of best fit
  x = range(df["Year"].iloc[0], 2051, 1)
  result = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
  plt.plot(x, result.intercept + result.slope*x, 'r', label='fitted line')

  # Create second line of best fit
  df2 = df[df['Year'] >= 2000]
  y = range(2000, 2051)
  result2000 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
  plt.plot(y, result2000.intercept + result2000.slope*y, 'r', label='fitted line 2')

  # Add labels and title
  plt.legend()
  plt.title("Rise in Sea Level")
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()