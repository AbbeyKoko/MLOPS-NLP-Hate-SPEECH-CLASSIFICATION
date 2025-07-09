import tensorflow as tf
import time

with tf.device('/GPU:0'):
    start = time.time()
    a = tf.random.normal([10000, 10000])
    b = tf.matmul(a, a)
    print("GPU time:", time.time() - start)

with tf.device('/CPU:0'):
    start = time.time()
    a = tf.random.normal([10000, 10000])
    b = tf.matmul(a, a)
    print("CPU time:", time.time() - start)
