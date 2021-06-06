import tensorflow as tf

mat = tf.constant([[1,1,1],[1,0,1],[1,1,1]])
mat_t = tf.transpose(mat)

print(mat == mat_t)
