import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# Loading the data

data = pd.read_csv('cleaned_data.csv')

# Check the first few head rows of the data to get a sense of what it looks like
print(data.head(3))

# Visualize the distribution of each column in the data set using histograms
data.hist(bins=50, figsize=(20,15))
plt.show()

