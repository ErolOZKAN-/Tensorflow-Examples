from __future__ import print_function
import tensorflow as tf

# CONSTANT ADDITION AND MULTIPICATION
a = tf.constant(2)
b = tf.constant(3)
sess = tf.Session()
print("a=2, b=3")
print("Addition with constants: %i" % sess.run(a+b))
print("Multiplication with constants: %i" % sess.run(a*b))

# VARIABLE ADDITION AND MULTIPICATION
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
add = tf.add(a, b)
mul = tf.multiply(a, b)
print("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))

# MATRIX MULTIPICATION
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.],[2.]])
product = tf.matmul(matrix1, matrix2)
result = sess.run(product)
print(result)

