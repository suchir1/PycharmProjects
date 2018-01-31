import tensorflow as tf
import numpy as np
import time

init_op = tf.global_variables_initializer()
sess = tf.InteractiveSession()


def create_file_reader_ops(filename_queue):
    reader = tf.TextLineReader(skip_header_lines=1)
    _, csv_row = reader.read(filename_queue)
    record_defaults = [[1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = tf.decode_csv(
        csv_row, record_defaults=record_defaults)
    features = tf.stack([col1, col2, col3, col4, col5, col6, col7, col8, col9])
    label = tf.stack([col10, col11])
    return features, label


filename_queue = tf.train.string_input_producer(["COMBINED_DATA.csv"])
features, labels = create_file_reader_ops(filename_queue)


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

start = time.time()
for i in range(500):
    features = tf.reshape(features, [1,9])
    labels = tf.reshape(labels, [1,2])
    train_step.run(feed_dict={x: sess.run(features), y_: sess.run(labels)})
end = time.time()

print(sess.run(W))

print(end-start)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

total_correct = 0.0
training_loops = 183
start = time.time()
for i in range(training_loops):
    features = tf.reshape(features, [1, 9])
    labels = tf.reshape(labels, [1, 2])
    total_correct += accuracy.eval(feed_dict={x: sess.run(features), y_: sess.run(labels)})

end = time.time()
print(end-start)
coord.request_stop()

print(total_correct/training_loops)

coord.join(threads)


sess.close()
