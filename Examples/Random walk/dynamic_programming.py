import numpy as np
from agent import random_policy
import matplotlib.pyplot as plt
from operator import truediv

returns=[0, 0, 0]
stateValue=[0, 0, 0]
recordStateValue=[]
#gamma=[0.2, 0.4, 0.6, 0.8, 1]
gamma=0.2
stepSize=0.1
n=[0,0,0]
actionProb=0.5

r=[[0,0], [0,0], [0,1]]

for i in range(1000):
    for x in [0,1,2]:
        left=x-1
        right=x+1
        if left<0:
            left=0
        if right>2:
            right=2

        stateValue[x] = actionProb*(r[x][1]+gamma*stateValue[left]) + actionProb*(r[x][1]+gamma*stateValue[right])


print(stateValue)
#recordStateValue = np.append(recordStateValue, stateValue)
# #print(recordStateValue)   
#plt.plot(recordStateValue)
#plt.plot(stateValue)
#plt.ylabel('State value')
#plt.xlabel('State')
#plt.title('Random walk')
#plt.legend(['gamma=0.2', 'gamma=0.4', 'gamma=0.6', 'gamma=0.8', 'gamma=1'])
#plt.show()
