'''
Preparing to train with Estimators
For this exercise, we'll return to the King County housing transaction dataset from chapter 2. We will again develop and train a machine learning model to predict house prices; however, this time, we'll do it using the estimator API.

Rather than completing everything in one step, we'll break this procedure down into parts. We'll begin by defining the feature columns and loading the data. In the next exercise, we'll define and train a premade estimator. Note that feature_column has been imported for you from tensorflow. Additionally, numpy has been imported as np, and the Kings County housing dataset is available as a pandas DataFrame: housing.

Instructions
100 XP
Complete the feature column for bedrooms and add another numeric feature column for bathrooms. Use bedrooms and bathrooms as the keys.
Create a list of the feature columns, feature_list, in the order in which they were defined.
Set labels to be equal to the price column in housing.
Complete the bedrooms entry of the features dictionary and add another entry for bathrooms.
'''
SOLUTION

# Define feature columns for bedrooms and bathrooms
bedrooms = feature_column.numeric_column("bedrooms")
bathrooms = feature_column.numeric_column('bathrooms')

# Define the list of feature columns
feature_list = [bedrooms, bathrooms]

def input_fn():
	# Define the labels
	labels = np.array(housing['price'])
	# Define the features
	features = {'bedrooms':np.array(housing['bedrooms']), 
                'bathrooms':np.array(housing['bathrooms'])}
	return features, labels