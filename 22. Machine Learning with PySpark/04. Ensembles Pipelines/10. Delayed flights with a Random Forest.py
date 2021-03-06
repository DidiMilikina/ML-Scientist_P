'''
Delayed flights with a Random Forest
In this exercise you'll bring together cross validation and ensemble methods. You'll be training a Random Forest classifier to predict delayed flights, using cross validation to choose the best values for model parameters.

You'll find good values for the following parameters:

featureSubsetStrategy — the number of features to consider for splitting at each node and
maxDepth — the maximum number of splits along any branch.
Unfortunately building this model takes too long, so we won't be running the .fit() method on the pipeline.

Instructions
100 XP
Create a random forest classifier object.
Create a parameter grid builder object. Add grid points for the featureSubsetStrategy and maxDepth parameters.
Create binary classification evaluator.
Create a cross-validator object, specifying the estimator, parameter grid and evaluator. Choose 5-fold cross validation.
'''
SOLUTION

# Create a random forest classifier
forest = RandomForestClassifier()

# Create a parameter grid
params = ParamGridBuilder() \
            .addGrid(forest.featureSubsetStrategy, ['all', 'onethird', 'sqrt', 'log2']) \
            .addGrid(forest.maxDepth, [2, 5, 10]) \
            .build()

# Create a binary classification evaluator
evaluator = BinaryClassificationEvaluator()

# Create a cross-validator
cv = CrossValidator(estimator=forest, estimatorParamMaps=params, evaluator=evaluator, numFolds=5)