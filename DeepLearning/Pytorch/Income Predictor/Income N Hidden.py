import torch
import numpy as np
import torch.utils.data as data_utils
from torch.autograd import Variable

accuracy_values = np.zeros(shape = (7,8))

for num_hidden_layers in range(5,6):
    for neuron_index in range(2,3):
        for loop in range(3):
            batch_size = 1000
            learning_rate = 1e-4
            epochs_training = 20
            dtype = torch.FloatTensor
            D_in, D_out = 88, 2
            hidden_layers = num_hidden_layers
            num_neuron_list = [64, 128, 256, 512, 1024, 2048]
            neurons = num_neuron_list[neuron_index]

            def prime_factors(n):
                primfac = []
                d = 2
                while d*d <= n:
                    while (n % d) == 0:
                        primfac.append(d)
                        n //= d
                    d += 1
                if n > 1:
                   primfac.append(n)
                return primfac

            def make_hidden_layers(hidden_layers, neurons):
                factors_list = prime_factors(neurons)
                factors_list.append(1)
                num_factors = len(factors_list)
                if(num_factors - 2 >= hidden_layers):
                    module_list = list()
                    module_list.append(torch.nn.Linear(D_in, neurons))
                    for i in range(hidden_layers):
                        module_list.append(torch.nn.ReLU())
                        module_list.append(torch.nn.Linear(int(neurons/factors_list[num_factors-i-1]), int(neurons/factors_list[num_factors-i-2])))
                    module_list.append(torch.nn.ReLU())
                    module_list.append(torch.nn.Linear(int(neurons/factors_list[num_factors-hidden_layers-1]), D_out))
                    module_list.append(torch.nn.Softmax())
                    return module_list
                else:
                    return

            file = "Income Prediction Data.csv"
            all_data = np.genfromtxt(file, delimiter=',', skip_header=1)
            training_features = all_data[:24000, 0:88]
            training_labels = all_data[:24000, 90]
            training_features = torch.from_numpy(training_features)
            training_labels = torch.from_numpy(training_labels)
            train = data_utils.TensorDataset(training_features, training_labels)
            train_loader = data_utils.DataLoader(train, batch_size=batch_size, shuffle=True)

            testing_features = all_data[24000:, 0:88]
            testing_labels = all_data[24000:, 90]
            testing_features = torch.from_numpy(testing_features)
            testing_labels = torch.from_numpy(testing_labels)
            test = data_utils.TensorDataset(testing_features, testing_labels)
            test_loader = data_utils.DataLoader(test, batch_size=len(testing_features), shuffle=False)
            try:
                model = torch.nn.Sequential(*make_hidden_layers(hidden_layers, neurons))
            except TypeError:
                continue

            model = model.cuda()
            loss_fn = torch.nn.CrossEntropyLoss()

            optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

            for epoch in range(epochs_training):
                epoch_loss = 0
                for t, batch in enumerate(train_loader):
                    features_batch, labels_batch = batch
                    features_batch, labels_batch = Variable(features_batch.type(dtype)).cuda(), Variable(labels_batch.type(torch.LongTensor)).cuda()
                    y_pred = model(features_batch)
                    loss = loss_fn(y_pred, labels_batch)
                    epoch_loss += loss
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()
                #print("Loss for epoch ", epoch, ": ", epoch_loss.data, sep="")

            correct = 0
            for batch in test_loader:
                features_batch, labels_batch = batch
                labels_batch = labels_batch.type(torch.LongTensor).cuda()
                features_batch = Variable(features_batch.type(dtype)).cuda()
                y_pred = model(features_batch)
                _, predicted = torch.max(y_pred.data, 1)
                correct += (predicted==labels_batch).sum()

            print("For", num_hidden_layers, "hidden layers and", num_neuron_list[neuron_index],"neurons, accuracy value is:", 100*correct/len(labels_batch))
            accuracy_values[neuron_index, num_hidden_layers] += 100*correct/len(labels_batch)
        accuracy_values[neuron_index, num_hidden_layers] = accuracy_values[neuron_index, num_hidden_layers] / 3


np.savetxt("Accuracy Values.csv", accuracy_values, delimiter="\t")