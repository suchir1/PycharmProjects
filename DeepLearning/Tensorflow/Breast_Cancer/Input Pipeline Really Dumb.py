import tensorflow as tf
import numpy as np

init_op = tf.global_variables_initializer()
sess = tf.InteractiveSession()


def read_csv(filename_queue):
    reader = tf.TextLineReader(skip_header_lines=1)
    _, csv_row = reader.read(filename_queue)
    record_defaults = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = tf.decode_csv(
        csv_row, record_defaults=record_defaults)
    features = tf.stack([col1, col2, col3, col4, col5, col6, col7, col8, col9])
    label = tf.stack([col10, col11])
    return features, label

def input_pipeline(filenames, batch_size, read_threads, num_epochs):
    filename_queue = tf.train.string_input_producer(filenames, num_epochs = num_epochs, shuffle = True)
    features, label = read_csv(filename_queue)
    print("1")
    min_after_dequeue = 100
    capacity = 700
    feature_batch, label_batch = tf.train.shuffle_batch([features, label], batch_size = batch_size, capacity = capacity, min_after_dequeue = min_after_dequeue)
    return feature_batch, label_batch



feature_batch, label_batch = input_pipeline(["TRAINING_DATA.csv"], 32, 1, None)


x = tf.placeholder(tf.float32, shape=[None, 9])
y_ = tf.placeholder(tf.float32, shape=[None, 2])

W = tf.Variable(tf.zeros([9, 2]))
b = tf.Variable(tf.zeros([2]))

y = tf.matmul(x,W) +b
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))



train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


sess.run(tf.global_variables_initializer())
sess.run(tf.local_variables_initializer())
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners( sess = sess, coord=coord)


for i in range(1000):
    #features = tf.reshape(features, [1,9])
    #labels = tf.reshape(labels, [1,2])
    train_step.run(feed_dict={x: sess.run(feature_batch), y_: sess.run(label_batch)})

print(sess.run(W))

testing_features, testing_labels = input_pipeline(["TESTING_DATA.csv"], 100, 1, 1)

print(sess.run(testing_features))

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(accuracy.eval(feed_dict={x: sess.run(testing_features), y_: sess.run(testing_labels)}))

coord.request_stop()


coord.join(threads)


sess.close()
