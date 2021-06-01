import tensorflow as tf
saver = tf.train.import_meta_graph('my_test_model-1000.meta')

with tf.Session() as sess:

    new_saver = tf.train.import_meta_graph('my_test_model-1000.meta')

    new_saver.restore(sess, tf.train.latest_checkpoint('./'))