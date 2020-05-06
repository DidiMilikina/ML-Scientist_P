'''
Do we need more data?
It's time to check whether the digits dataset model you built benefits from more training examples!

In order to keep code to a minimum, various things are already initialized and ready to use:

The model you just built.
X_train,y_train,X_test, and y_test.
The initial_weights of your model, saved after using model.get_weights().
A defined list of training sizes: training_sizes.
A defined EarlyStopping callback monitoring loss: early_stop.
Two empty lists to store the evaluation results: train_accs and test_accs.
Train your model on the different training sizes and evaluate the results on X_test. End by plotting the results with plot_results().

The full code for this exercise can be found on the slides!

Instructions
100 XP
Get a fraction of the training data determined by the size we are currently evaluating in the loop.
Set the model weights to the initial_weights with set_weights() and train your model on the fraction of training data using early_stop as a callback.
Evaluate and store the accuracy for the training fraction and the test set.
Call plot_results() passing in the training and test accuracies for each training size.
'''
SOLUTION

for size in train_sizes:
  	# Get a fraction of training data (we only care about the training data)
    X_train_frac, X_test_frac, y_train_frac, y_test_frac = train_test_split(
      X_train, y_train, train_size = size)
    # Set the model weights and fit the model on the training data
    model.set_weights(initial_weights)
    model.fit(X_train_frac, y_train_frac, epochs = 50, callbacks = [early_stop])

    # Evaluate and store the train fraction and the complete test set results
    train_accs.append(model.evaluate(X_train_frac, y_train_frac)[1])
    test_accs.append(model.evaluate(X_test_frac, y_test_frac)[1])

# Plot train vs test accuracies
plot_results(train_accs, test_accs)