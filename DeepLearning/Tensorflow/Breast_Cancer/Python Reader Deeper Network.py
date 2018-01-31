import tensorflow as tf
import time
import os

sess = tf.InteractiveSession()

dir_path = os.path.dirname(os.path.realpath(__file__))


def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

def forwardprop(X, w_1, w_2, w_3):
    h = tf.nn.relu(tf.matmul(X, w_1))
    h_1 = tf.nn.relu(tf.matmul(h, w_2))  # The \varphi function
    yhat = tf.matmul(h_1, w_3)
    return yhat

x = tf.placeholder(tf.float32, shape=[1, 9])
y_ = tf.placeholder(tf.float32, shape=[1, 2])

w_1 = weight_variable([9,2])
w_2 = weight_variable([2, 9])
w_3 = weight_variable([9,2])

b_1 = bias_variable([2])

# Forward propagation
y = forwardprop(x, w_1, w_2,w_3) + b_1
predict = tf.argmax(y, axis=1)

# Backward propagation
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
updates = tf.train.GradientDescentOptimizer(.01).minimize(cost)



sess.run(tf.global_variables_initializer())

for loops in range(5):

    filename = dir_path + "/TRAINING_DATA.csv"

    start = time.time()
    with open(filename) as inf:
        inf.seek(0)
        next(inf)
        for line in inf:
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = line.strip().split(',')
            features = tf.stack([col1, col2, col3, col4, col5, col6, col7, col8, col9])
            label = tf.stack([col10, col11])
            features = tf.reshape(features, [1, 9])
            label = tf.reshape(label, [1, 2])
            updates.run(feed_dict={x: sess.run(features), y_: sess.run(label)})

    end = time.time()
    print(end - start)


    filename = dir_path + "/TESTING_DATA.csv"
    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    i = 0
    total_correct = 0
    start = time.time()
    with open(filename) as inf:
        inf.seek(0)
        next(inf)
        for line in inf:
            i+=1
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = line.strip().split(',')
            features = tf.stack([col1, col2, col3, col4, col5, col6, col7, col8, col9])
            label = tf.stack([col10, col11])
            features = tf.reshape(features, [1, 9])
            label = tf.reshape(label, [1, 2])
            total_correct+=accuracy.eval(feed_dict={x: sess.run(features), y_: sess.run(label)})


    print("Accuracy for loop", loops, ":", total_correct/i)

    end = time.time()
    print(end - start)


sess.close()