'''
Build as shown!
You will take on a final challenge before moving on to the next lesson. Build the network shown in the picture below. Prove your mastered Keras basics in no time!


Instructions
100 XP
Instantiate a Sequential model.
Build the input and hidden layer.
Add the output layer.
'''
SOLUTION

from keras.models import Sequential
from keras.layers import Dense

# Instantiate a Sequential model
model = Sequential()

# Build the input and hidden layer
model.add(Dense(3, input_shape=(2,), activation='relu'))

# Add the ouput layer
model.add(Dense(1))