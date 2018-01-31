import pandas as pd

filename = "/home/cheesecake/PycharmProjects/DeepLearning/Pytorch/Income Predictor/CategoricalData"



with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

pd.DataFrame.to_clipboard(pd.get_dummies(content))