import tensorflow as tf

mat = tf.reshape(tf.range(20),(5,4))

# Calculate transpose

mat_t = tf.transpose(mat)