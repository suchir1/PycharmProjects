import torch
import numpy as np
import torch.utils.data as data_utils
from torch.autograd import Variable

batch_size = 1000
learning_rate = 1e-2
epochs_training = 20
dtype = torch.FloatTensor
D_in, H, D_out = 88, 1000, 2

file = "Income Prediction Data.csv"
all_data = np.genfromtxt(file, delimiter=',', skip_header=1)
training_features = all_data[:29000, 0:88]
training_labels = all_data[:29000, 90]
training_features = torch.from_numpy(training_features)
training_labels = torch.from_numpy(training_labels)
train = data_utils.TensorDataset(training_features, training_labels)
train_loader = data_utils.DataLoader(train, batch_size=batch_size, shuffle=True)

testing_features = all_data[29000:, 0:88]
testing_labels = all_data[29000:, 90]
testing_features = torch.from_numpy(testing_features)
testing_labels = torch.from_numpy(testing_labels)
test = data_utils.TensorDataset(testing_features, testing_labels)
test_loader = data_utils.DataLoader(test, batch_size=len(testing_features), shuffle=False)

model = torch.nn.Sequential(
    torch.nn.Linear(D_in, H),
    torch.nn.ReLU(), torch.nn.Linear(H, D_out),
     torch.nn.Softmax()
)
loss_fn = torch.nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(epochs_training):
    epoch_loss = 0
    for t, batch in enumerate(train_loader):
        features_batch, labels_batch = batch
        features_batch, labels_batch = Variable(features_batch.type(dtype)), Variable(labels_batch.type(torch.LongTensor))
        y_pred = model(features_batch)
        loss = loss_fn(y_pred, labels_batch)
        epoch_loss += loss
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print("Loss for epoch ", epoch, ": ", epoch_loss.data, sep="")

correct = 0
for batch in test_loader:
    features_batch, labels_batch = batch
    labels_batch = labels_batch.type(torch.LongTensor)
    features_batch = Variable(features_batch.type(dtype))
    y_pred = model(features_batch)
    _, predicted = torch.max(y_pred.data, 1)
    correct += (predicted==labels_batch).sum()

print(100*correct/len(labels_batch))
