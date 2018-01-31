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
features = torch.from_numpy(features)
labels = torch.from_numpy(labels)
train = data_utils.TensorDataset(features, labels)
train_loader = data_utils.DataLoader(train, batch_size=batch_size, shuffle=True)

# D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
D_in, H, D_out = 9, 100, 2

w1 = Variable(torch.randn(D_in, H).type(dtype), requires_grad=True)
w2 = Variable(torch.randn(H, D_out).type(dtype), requires_grad=True)


def compute_y_(features_batch, w1, w2):
    h = features_batch.mm(w1)
    h_relu = h.clamp(min=0)
    y_ = h_relu.mm(w2)
    return y_


loss_fn = torch.nn.MSELoss(size_average=False)
for epoch in range(epochs_training):
    epoch_loss = 0
    for i, batch in enumerate(train_loader):
        features_batch, labels_batch = batch
        features_batch, labels_batch = Variable(features_batch), Variable(labels_batch)
        y_ = compute_y_(features_batch, w1, w2)
        loss = loss_fn(y_, labels_batch)
        epoch_loss += loss.data[0]
        loss.backward()
        w1.data -= learning_rate * w1.grad.data
        w2.data -= learning_rate * w2.grad.data
        w1.grad.data.zero_()
        w2.grad.data.zero_()

file = "TESTING_DATA.csv"
all_data = np.genfromtxt(file, delimiter=',', skip_header=1)
features = all_data[:, 0:9]
labels = all_data[:,9:11]
features = torch.from_numpy(features)
labels = torch.from_numpy(labels)
test = data_utils.TensorDataset(features, labels)
test_loader = data_utils.DataLoader(train, batch_size=batch_size, shuffle=True)

for batch in test_loader:
    features_batch, labels_batch = batch
    features_batch, labels_batch = Variable(features_batch), Variable(labels_batch)
    y_ = compute_y_(features_batch, w1, w2)
    print(labels_batch)