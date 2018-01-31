# Code in file nn/two_layer_net_optim.py
import torch
import numpy as np
import torch.utils.data as data_utils
from torch.autograd import Variable

dtype = torch.FloatTensor
batch_size = 50
learning_rate = 1e-4
epochs_training = 5

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
D_in, H, D_out = 9, 100, 2

file = "/home/cheesecake/PycharmProjects/DeepLearning/Pytorch/Breast Cancer/TRAINING_DATA.csv"
all_data = np.genfromtxt(file, delimiter=',', skip_header=1)
features = all_data[:, 0:9]
labels = all_data[:,9:11]
features = torch.from_numpy(features)
labels = torch.from_numpy(labels)
train = data_utils.TensorDataset(features, labels)
train_loader = data_utils.DataLoader(train, batch_size=batch_size, shuffle=True)

# Use the nn package to define our model and loss function.
model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(), torch.nn.Linear(H, D_out),
     torch.nn.Softmax()
)
loss_fn = torch.nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
for epoch in range(epochs_training):
    for t, batch in enumerate(train_loader):
        features_batch, labels_batch = batch
        features_batch = Variable(features_batch.type(dtype))
        y_pred = model(features_batch)
        labels_batch = labels_batch.numpy()
        idxs = np.where(labels_batch > 0)[1]
        new_targets = Variable(torch.from_numpy(idxs).type(dtype), requires_grad = True)
        print(new_targets)
        loss = loss_fn(y_pred, new_targets)
        #print(t, loss.data[0])
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


testing_file = "TESTING_DATA.csv"
testing_data = np.genfromtxt(testing_file, delimiter=',', skip_header=1)
testing_features = testing_data[:, 0:9]
testing_labels = testing_data[:, 9:11]
testing_features = torch.from_numpy(testing_features)
testing_labels = torch.from_numpy(testing_labels)
test = data_utils.TensorDataset(testing_features, testing_labels)
test_loader = data_utils.DataLoader(test, batch_size=100)

for t, test_batch in enumerate(test_loader):
    features_batch, labels_batch = test_batch
    features_batch, labels_batch = Variable(features_batch.type(dtype)), Variable(labels_batch.type(dtype))
    y_pred = model(features_batch)
    length = len(y_pred)
    print(y_pred)
    for i in range(length):
        value, index = y_pred[i].max(0)
        y_pred[i][index] = 1
        y_pred[i][(index+1)%2] = 0
    print(y_pred)

