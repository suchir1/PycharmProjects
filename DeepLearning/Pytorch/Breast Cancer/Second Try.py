import torch
import numpy as np
import torch.utils.data as data_utils
from torch.autograd import Variable

batch_size = 50
learning_rate = 1e-4
epochs_training = 1
dtype = torch.DoubleTensor

file = "TRAINING_DATA.csv"
all_data = np.genfromtxt(file, delimiter=',', skip_header=1)
features = all_data[:, 0:9]
labels = all_data[:,9:11]
features = Variable(torch.from_numpy(features).type(dtype))
labels = Variable(torch.from_numpy(labels).type(dtype))

# D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
D_in, H, D_out = 9, 100, 2

w1 = Variable(torch.randn(D_in, H).type(dtype), requires_grad=True)
w2 = Variable(torch.randn(H, D_out).type(dtype), requires_grad=True)


def compute_y_(features, w1, w2):
    h = features.mm(w1)
    h_relu = h.clamp(min=0)
    y_ = h_relu.mm(w2)
    return y_

epoch_loss = 0
loss_fn = torch.nn.MSELoss(size_average=False)
for epoch in range(epochs_training):
    compute_y_
    y_ = compute_y_(features, w1, w2)
    print(y_)
    loss = loss_fn(y_, labels)
    if epoch:
        w1.grad.data.zero_()
        w2.grad.data.zero_()
    epoch_loss += loss.data[0]
    loss.backward()
    w1.data -= learning_rate * w1.grad.data
    w2.data -= learning_rate * w2.grad.data



file = "TESTING_DATA.csv"
all_data = np.genfromtxt(file, delimiter=',', skip_header=1)
features = all_data[:, 0:9]
labels = all_data[:,9:11]
features = torch.from_numpy(features)
features = Variable(features)
labels = torch.from_numpy(labels)
labels = Variable(labels)


y_1 = compute_y_(features, w1, w2)
print(labels)
