import tensorflow as tf

if __name__ == '__main__':
    hello = tf.constant("Hello world")
    tf.constant("Who am I")
    sess = tf.Session()
    print(sess.run(hello))
