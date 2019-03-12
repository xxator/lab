from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt 
import csv
import pandas as pd 
from random import sample

def change(a):
    if a == "yes":
        return 1
    return 0


filename = "housing.csv"
raw_data = open(filename, 'rt')
df = pd.read_csv(filename)

df.drop("Unnamed: 0",axis=1,inplace=True)
df['driveway'] = df['driveway'].apply(change)
df['recroom'] = df['recroom'].apply(change)
df['fullbase'] = df['fullbase'].apply(change)
df['gashw'] = df['gashw'].apply(change)
df['airco'] = df['airco'].apply(change)
df['prefarea'] = df['prefarea'].apply(change)

train = df[41:541]
test = df[0:40]
#print(test)
print(train.shape,test.shape)
result = train['price']
train.drop("price",axis = 1 , inplace = True)

train = (train-train.mean())/(train.std())

data = np.asarray(train)
print(data)


def predict(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i + 1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0



# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0.0
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			sum_error += error**2
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
	return weights
 
# # Calculate weights
# dataset = [[2.7810836,2.550537003,0],
# 	[1.465489372,2.362125076,0],
# 	[3.396561688,4.400293529,0],
# 	[1.38807019,1.850220317,0],
# 	[3.06407232,3.005305973,0],
# 	[7.627531214,2.759262235,1],
# 	[5.332441248,2.088626775,1],
# 	[6.922596716,1.77106367,1],
# 	[8.675418651,-0.242068655,1],
# 	[7.673756466,3.508563011,1]]
# l_rate = 0.1
# n_epoch = 5
# weights = train_weights(dataset, l_rate, n_epoch)
# print(weights)