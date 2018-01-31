import tensorflow as tf
import time
import os

sess = tf.InteractiveSession()

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/TRAINING_DATA.csv"

x = tf.placeholder(tf.float32, shape=[1, 9])
y_ = tf.placeholder(tf.float32, shape=[1, 2])

W = tf.Variable(tf.zeros([9, 2]))
b = tf.Variable(tf.zeros([2]))

y = tf.matmul(x,W) +b
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess.run(tf.global_variables_initializer())

with open(filename) as inf:
    next(inf)
    for line in inf:
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = line.strip().split(',')
        features = tf.stack([col1, col2, col3, col4, col5, col6, col7, col8, col9])
        label = tf.stack([col10, col11])
        features = tf.reshape(features, [1, 9])
        label = tf.reshape(label, [1, 2])
        train_step.run(feed_dict={x: sess.run(features), y_: sess.run(label)})


print(sess.run(W))

filename = dir_path + "/TESTING_DATA.csv"
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

i = 0
total_correct = 0
with open(filename) as inf:
    next(inf)
    for line in inf:
        i+=1
        col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = line.strip().split(',')
        features = tf.stack([col1, col2, col3, col4, col5, col6, col7, col8, col9])
        label = tf.stack([col10, col11])
        features = tf.reshape(features, [1, 9])
        label = tf.reshape(label, [1, 2])
        total_correct+=accuracy.eval(feed_dict={x: sess.run(features), y_: sess.run(label)})

print(total_correct/i)