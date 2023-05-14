import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

class VisualizationEngine:
  def __init__(self, dataset):
    self.dataset = dataset
    self.barplot = None
    self.df_by_feature = None
    self.count_list = None
  
  # Create a slice of a data from a certain feature during a specific year
  def create_slice(self, feature, year):
    return (self.dataset[feature] == year)
  
  # Get data from a slice
  def get_data_from_slice(self, slice):
    return self.dataset[slice]

  # Get a total count of a feature from a dataset slice from a year
  def get_total_count(self, feature, dataset):
    self.df_by_feature = pd.DataFrame(dataset[feature].value_counts())
    return pd.DataFrame(dataset[feature].value_counts())

  # Helper function for creating a barplot
  def barplot(x, y, color):
    fig = plt.figure(figsize = (12, 6))
    bp = plt.bar(x, y, color=color, width = 0.5)
    return bp
  
  # Create a count list of each feature provided compared to our dataframe
  def create_count_list(self, feature):
    count_list = []
    for count in self.df_by_feature[feature]:
      count_list.append(count)
    self.count_list = count_list
    return count_list

  # Create a barplot (user must provide list of features by feature in that year ex: genres_2006 = ['Action', 'Sports', 'Role-Playing', 'Misc', 'Racing', 'Adventure', 'Shooter', 'Simulation', 'Fighting', 'Platform', 'Puzzle', 'Strategy'], and a color)
  def create_barplot(self, features_by_year_list, color, xlabel, ylabel, title):
    self.barplot = barplot(features_by_year_list, self.count_list, color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

  # Create a horizontal barplot using our existing barplot
  def create_horizontal_bp(xlabel, ylabel, title, platforms, total_games):
    plt.figure(figsize=(10,8))
    sns.barplot(y=platforms, x=total_games, orient='h').set(title=title)
    plt.ylabel = ylabel
    plt.xlabel = xlabel
    
  # Create a heatmap with our current data
  def create_heatmap(self, columns_list, color, title):
    # Initialize plotting boundaries
    plt.figure(figsize=(10, 8))

    # Set parameters
    needed_cols = columns_list
    # Generate heatmap
    sns.heatmap(self.dataset[needed_cols].corr().round(4), annot=True, cmap=color, square=True)

    # Set title for correlation matrix
    plt.title(title)