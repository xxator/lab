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

df = (df-df.mean())/df.std()

train = df.iloc[41:541]
#(train,'\n')

test = df.iloc[0:40]
#print(test)
print(train.shape,test.shape)
result = train['price']
train.drop("price",axis = 1 , inplace = True)
G  = np.asmatrix(train.values)
X = G.astype(float)
K = np.zeros((X.shape))

X = np.hstack((np.ones((500,1)) , X))
Y = np.asmatrix(result.values)
Y = Y.reshape(500,1)

def linear_theta(X,Y,lamb,l):
	theta = np.linalg.pinv(np.add(np.transpose(X)@X,lamb*l))@(np.transpose(X)@Y)
	return theta

def gradient_descent(X,Y,iters):
	alpha = 0.001
	Xtrans = X.transpose()
	theta = np.zeros(X.shape[1])
	theta = np.asmatrix(theta)
	theta = theta.transpose()
	for i in range(iters):
			diffs = np.dot(X,theta)-Y
			gradient = np.dot(Xtrans,diffs)/len(X)
			print(theta-(alpha*gradient))
			theta = theta-(alpha*gradient)
	return theta


optimum_lambda = 500
min_error = 100
p = test['price']
prices = np.asmatrix(p.values)
test.drop("price",axis = 1 , inplace = True)
test = np.hstack((np.ones((40,1)) , test))
row,col = test.shape
#print(prices)
# for i in range(0,20):
# 	lamb = np.identity(X.shape[1])
# 	lamb[0][0] = 0
# 	l = i*100
# 	theta = linear_theta(X,Y,lamb,l)	
# 	cumulative_error = 0
# 	for i in range(row):
# 		predicted = (np.asmatrix(test[i])@theta).item(0,0)	
# 		temp = (abs(predicted-prices.item(0,i))/prices.item(0,i))*100
# 		cumulative_error += temp 	
# 	cumulative_error = (cumulative_error/40.0)
# 	print(cumulative_error,'%')
# 	if cumulative_error < min_error:
# 		min_error = cumulative_error
# 		optimum_lambda = l
# for i in range(0,20):
# 	lamb = np.identity(X.shape[1])
# 	lamb[0][0]=0
# 	l = i*100
# 	theta = gradient_descent(X,Y,100*(i+1))	
# 	cumulative_error = 0
# 	for i in range(row):
# 		predicted = (np.asmatrix(test[i])@theta).item(0,0)	
# 		temp = (abs(predicted-prices.item(0,i))/prices.item(0,i))*100
# 		cumulative_error += temp 	
# 	cumulative_error = (cumulative_error/40.0)
# 	print(cumulative_error,'%')
# 	if cumulative_error < min_error:
# 		min_error = cumulative_error
# 		optimum_lambda = l
lamb = np.identity(X.shape[1])
lamb[0][0] = 0
testo = linear_theta(X,Y,lamb,10)

theta = gradient_descent(X,Y,100000)	

cumulative_error = 0
for i in range(row):
	predicted = (np.asmatrix(test[i])@theta).item(0,0)	
	temp = (abs(predicted-prices.item(0,i))/prices.item(0,i))*100
	cumulative_error += temp 	
cumulative_error = (cumulative_error/row)
print(cumulative_error,'%')

# print("min error: ",min_error,"  lambda : ",optimum_lambda)









