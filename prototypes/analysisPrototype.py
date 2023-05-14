import numpy as np
import pandas as pd

class AnalysisEngine:
  def __init__(self, path):
    self.path = path
    self.dataset = None
    self.features = None
    self.descriptors = None
    self.ref_path = None
    self.data_dict = None

  # Read in path to create dataset
  def read(self):
    self.dataset = pd.read_csv(self.path)

  # Return first five rows of the dataset
  def get_sample(self):
    return self.dataset.head()

  # Return the shape (rows x columns) of the dataset
  def get_shape(self):
    return np.shape(self.dataset)
  
  # Return basic info of the dataset
  def get_info(self):
    return self.dataset.info()

  # Check the total number of null values in each feature of the dataset
  def detect_null_values(self):
    return self.dataset.isna().sum()

  # Print the total percentage of null data for the given features (list)
  def describe_null_data(self, features: list):
    total_rows = self.check_head()[0]
    for feature in features:
      # Grab total nulls in the passed feature
      null_data_total = self.detect_null_values()[feature]
      
      null_data_percentage = (null_data_total / total_rows) * 100
      print(f'Percentage of "{feature}" null data: {null_data_percentage}%')
  
  # Set features as a list of all the dataset's features
  def set_features(self):
    self.features = self.dataset.columns.tolist()
  
  # Set descriptors attribute to a list of given user descriptions of each feature 
  def set_descriptors(self, descriptions: list):
    self.descriptors = descriptions
  
  #Set refpatht attribute to given ref path from user
  def set_refpath(self, ref):
    self.ref_path = ref

  # Data dictionary creator
  def operate_data_dictionary(features, descriptors, method="set", refpath=None):
    """ Operational function to work in creating or getting data dictionary. """
    if method == "set":
      # Produce dictionary-wrapped key-value associations of feature summaries
      data_dictionary = dict(zip(features, descriptors))
      # Convert data dictionary to cleaner reference table
      reference = pd.DataFrame(data_dictionary, index=[0])
      # Save reference table for future access
      if refpath is not None and type(refpath) == str:
        reference.to_csv(refpath, index=False)
    if method == "get":
      # Get reference table from saved data dictionary
      if refpath is not None and type(refpath) == str:
        return pd.read_csv(refpath)
      else:
        raise TypeError("Saved file for data dictionary not found.")

  # Create a data dictionary
  def create_data_dictionary(self):
    self.data_dict = self.operate_data_dictionary(features=self.features, descriptors=self.descriptors, method="set", refpath=self.ref_path)
    return self.data_dict
  
  # Show a table of a reference of our dataset
  def show_table(self):
    reference = self.data_dict
    return reference.T