'''
Preparing a model for tuning
Let's tune the hyperparameters of a binary classification model that does well classifying the breast cancer dataset.

You've seen that the first step to turn a model into a sklearn estimator is to build a function that creates it. This function is important since you can play with the parameters it receives to achieve the different models you'd like to try out.

Build a simple create_model() function that receives a learning rate and an activation function as parameters. The Adam optimizer has been imported as an object from keras.optimizers so that you can change its learning rate parameter.

Instructions
100 XP
Set the learning rate of the Adam optimizer to the one passed in the parameters.
Set the hidden layers activations to the one passed in the parameters.
Pass the optimizer and the binary cross-entropy loss to the .compile() method.
'''
SOLUTION

# Creates a model given an activation and learning rate
def create_model(learning_rate=0.01, activation='relu'):
  
  	# Create an Adam optimizer with the given learning rate
  	opt = Adam(lr=0.01)
  	
  	# Create your binary classification model  
  	model = Sequential()
  	model.add(Dense(128, input_shape=(30,), activation='relu'))
  	model.add(Dense(256, activation='relu'))
  	model.add(Dense(1, activation='sigmoid'))
  	
  	# Compile your model with your optimizer, loss, and metrics
  	model.compile(optimizer=opt, loss='cross_entrophy', metrics=['accuracy'])
  	return model
