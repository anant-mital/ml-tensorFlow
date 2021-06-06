import tensorflow as tf

x = tf.constant([2], dtype = "float")
y = tf.constant([3], dtype = "float")

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)