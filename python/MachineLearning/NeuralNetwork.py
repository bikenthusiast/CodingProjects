import warnings
warnings.filterwarnings('ignore')
import tensorflow as tf
import numpy as np
# Compute follwoing example: y=(a+b)*x using tensorflow

# Define constants
a = tf.constant(1.0, name="a")
b = tf.constant(2.0, name="b")

# Define input
x = tf.placeholder(tf.float32, name="x")

# Define operations
sum_ab = tf.add(a, b)
y = tf.multiply(sum_ab, x)

# Create initialization operation
ini = tf.global_variables_initializer()

# Create input data
x_in = np.linspace(-5, 5, 6)  # 6 equally spaced numbers from -5 to 5 (i.e. [-5, -3, -1, 1, 3, 5])
x_in = x_in[:,np.newaxis]

# Run session
with tf.Session() as sess:
    # Execute graph
    sess.run(ini)
    out = sess.run(y, feed_dict={x: x_in})

    # Print result
    print("y = \n", out)