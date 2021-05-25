#importing some libraries we will use
import tensorflow as tf
import numpy as np

#using the mnist dataset
mnist = tf.keras.datasets.mnist

#dividing the data into training and testing sets
(training_data, training_labels), (test_data, test_labels) = mnist.load_data()
training_data, test_data = training_data / 255, test_data / 255

#creating the model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#training the model
model.fit(training_data, training_labels, epochs=5)

#testing our model
model.evaluate(test_data, test_labels)

predictions = model.predict(test_data)
np.set_printoptions(suppress=True)
print(test_labels[0])
print(predictions[0])
