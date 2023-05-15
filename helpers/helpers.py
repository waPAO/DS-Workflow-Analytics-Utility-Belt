import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Create and Read a Dataset Helper
def readDataset(path):
  DATAPATH = "penguins_simplified.csv"

  df = pd.read_csv(DATAPATH)
  dataset = df.copy()
  dataset.info()

  return dataset

# Encode Categorical Features Helper
def encodeCategoricalFeatures(dataset, feature, encoding="label"):
  """ Custom function to encode categorical features using label-schema. """
  # Instantiate encoder architecture
  if encoding == "label":
    encoder = LabelEncoder()
  # Transform dataset feature using labeling schema (performs in-place)
  dataset[feature] = encoder.fit_transform(dataset[feature])
  # Get fitted encoder (just in case)
  return encoder

# Impute Null Values Helper
def imputeNullVals(dataset, features):
  imputer = SimpleImputer(strategy="most_frequent")
  dataset.iloc[:, :] = imputer.fit_transform(dataset)
  encoders = dict.fromkeys(features)
  for key in encoders.keys():
    encoders[key] = encodeCategoricalFeatures(dataset=dataset, feature=key, encoding="label")

# Create Descriptors For Data Dictionary Helper
def createDescriptors(dataset):
  features = dataset.columns.tolist()
  descriptors = []

  # collect user defined descriptors
  for feature in features:
    descriptor = input(f"Please write a descriptor for: {feature}\n")
    descriptors.append(descriptor)

  return descriptors

# Data Dictionary Helper
def operateDataDictionary(features, descriptors, method="set", refpath=None):
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

#Barplot Helper  
def barplot(x, y, color):
  fig = plt.figure(figsize = (12, 6))
  bp = plt.bar(x, y, color=color, width = 0.5)
  
  return bp

  