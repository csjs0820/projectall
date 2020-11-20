from random import *
import numpy as np

datasetx = []
datasety = []
count1 = 0
count2 = 0
datasetx = np.random.binomial(n=1, p=0.5, size=2500)
datasety = np.random.binomial(n=1, p=0.5, size=2500)
for j in range(0, 2500):
    if datasetx[j] == 0:
        datasetx[j] = 263
        datasety[j] = 1
        count1 = count1 + 1
    else:
        datasetx[j] = 176
        datasety[j] = 0
        count2 = count2 + 1

testsetx = []
testsety = []
count3 = 0
count4 = 0
testsetx = np.random.binomial(n=1, p=0.5, size=100)
testsety = np.random.binomial(n=1, p=0.5, size=100)

print(testsetx)
for j in range(0, 100):
    if testsetx[j] > 0.5:
        testsetx[j] = 260
        testsety[j] = 1
        count3 = count3 + 1
    else:
        testsetx[j] = 160
        testsety[j] = 0
        count4 = count4 + 1
print(datasetx)
print(datasety)
print(testsetx)
print(testsety)