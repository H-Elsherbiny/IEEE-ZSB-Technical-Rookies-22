import tensorflow as tf
import numpy as np

mnist = tf.keras.dataset.mnsit

(x_train, y_train), (x_test,y_test) = mnist.load.data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequntial()
model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='spare_catagorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)
model.save('epic_num_reader_model')

new_model = tf.keras.models.load_model('epic_num_reader_model')
predictions = new_model.predict([x_test])

print(np.argmax(predictions[0]))