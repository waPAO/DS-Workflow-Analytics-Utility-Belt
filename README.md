# THE ALL IN ONE DATA SCIENCE UTILITY BELT FOR DS NOOBS LIKE ME
## Prototypic Engines
* **Analysis Engine**: Contains and allows for most of the basic steps and setup of a dataset. You will be able to have access to dataset features (via OOP attributes) and custom dataset functions like being able to and describe null data, create data dictionaries, and display reference tables.

* **Visualization Engine**: Allows for the creation of basic data analytics visualiztions, although if used properly, it can create really strong visuals to represent your data and discoveries. Feel free to edit and rearrange any of the set parameters with the class.

* **Web Scraping Engine**: This class uses selenium in order to create a Chrome Driver that will be used to setup and allow for scraping of the site you provide. Through this engine, you will be able to set up and create double-series CSVs.
*CAUTION - The class is setup to run only on Chrome and not any other browser. This class requires setup in order to be used. Be sure to download and navigate the path of your Chrome driver which can be found and downloaded via (ChromeDriver)[https://chromedriver.chromium.org/downloads] (Please make sure to install the proper version based on your current version of Chrome).

## Helper Methods
1. readDataset() - Allows users to create and have access to a dataset via a provided path and will print to your console the basic info of our dataset.

2. encodeCategoricalFeatures() - Allows the users to encode a feature in your dataset via LabelEncoder.

3. imputeNullVals() - Will impute the null vals in your dataset based on the null-features passed via a list/array as the second argument in the function.

4. createDescriptors(): Lets users create a list of descriptors for each feature in the dataset you pass in.

5. operateDataDictionary() - Makes use of the descriptors built in createDescriptors() and uses those in order to create a data dictionary of your dataset.

6. barplot() - is a simple visualization tool that can create quick barplots for your discoveries.

## Glossary
Goes over some fundamental and introductory terms of Data Science and Statistical practices!



