

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('data_exam.txt',sep=',') #reading the data

data.head()

w= np.ones(3) #setting w0,w1..
a= 0.01 #alpha
it=1000 #iterator = 1000 

x = data.iloc[0:70,0:2].values
x=(x-x.mean())/(x.std())
one_mat = np.ones([70,1])
x = np.concatenate((one_mat,x),axis=1) 
y = data.iloc[0:70,2].values


# cost function
def find_cost(x,y,w):
    g=1/(1+np.exp(-1*x.dot(w)))
    sum=0
    for i in range(len(y)):
        valx=y[i]*np.log(g[i])+(1-y[i])*np.log(1-g[i])
        sum+=valx
    return sum/(-1*len(x))

def gd(x,y,w,it,a):
#     cost = np.zeros(it)
    x_trans = x.T
    for i in range(it):
        dif = (1/(1+np.exp(-1*x.dot(w))))- y
        grad = np.dot(x_trans, dif) / len(x)
        w= w-a*grad
#         cost[i] = find_cost(x, y, w)    
    return w #,cost

#calling gd function and find_cost function
weights= gd(x,y,w,it,a)
print("regression parameters: ",weights)
final_cost = find_cost(x,y,weights)
print("final cost: ",final_cost)



# testing data
x1=data.iloc[70:101,0:2]
x1=(x1-x1.mean())/(x1.std())

one_mat = np.ones([30,1])
x1 = np.concatenate((one_mat,x1),axis=1)
gz=1/(1+np.exp(-1*(x1.dot(w))))
gz = [0 if x < 0.5 else 1 for x in gz]
print(gz)



y1=data.iloc[70:101,2].values
c=0
for i in range(0,30):
    if(gz[i]!=y1[i]):
        c=c+1        
print("Total errors:",c)  
        



lam=1000
w= np.ones(3)


def gd1(x,y,w,it,a):
#     cost = np.zeros(it)
    x_trans = x.T
    for i in range(it):
        dif = (1/(1+np.exp(-1*x.dot(w))))- y
        grad = np.dot(x_trans, dif) / len(x)
        w= w*(1-(a*lam/len(x)))-a*grad
#         cost[i] = find_cost(x, y, w)    
    return w #,cost

#calling gd function and find_cost function
weights= gd1(x,y,w,it,a)
print("regression parameters: ",weights)
final_cost = find_cost(x,y,weights)
print("final cost: ",final_cost)



gz=1/(1+np.exp(-1*(x1.dot(w))))
gz = [0 if x < 0.5 else 1 for x in gz]
print(gz)


c=0
for i in range(0,30):
    if(gz[i]!=y1[i]):
        c=c+1        
print("Total errors:",c)  


print("-----------------delta learning--------------------")



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
 
d = data.iloc[0:70,0:3].values
# d = (d-d.mean())/d.std()
dataset = np.asarray(d)

# Calculate weights
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
l_rate = 1
n_epoch = 200000
weights = train_weights(dataset, l_rate, n_epoch)
# print(weights)
w = [-5102.20000000103, 46.55513676856127, 42.1065791273505]
delta_prediction = []
t = data.iloc[70:101,0:2].values
ty = data.iloc[70:101,2].values
print(ty) 
test = np.asarray(t)
for row in test:
        prediction = predict(row, weights)
        delta_prediction.append(prediction)
print(delta_prediction)
