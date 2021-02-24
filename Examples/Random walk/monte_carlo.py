import numpy as np
from agent import random_policy
import matplotlib.pyplot as plt
from operator import truediv

returns=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
stateValue=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
recordStateValue=[]
gamma=[0.2, 0.4, 0.6, 0.8, 1]
#gamma=0.1
seenStates=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
stepSize=0.1
n=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for j in gamma:
    for y in range(1000):
        state=0
        seenStates=[0,0,0,0,0,0,0,0,0,0]
        history=[]
        t=0
        #returns=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        while state<10:
            t=t+1
            direction = random_policy()

            if direction == 'l':
                newstate = state-1
            elif direction == 'r':
                newstate = state+1

            if newstate<0:
                newstate=0

            if newstate==10:
                reward=0
            elif newstate!=10:
                reward=-1

            history.append([state, direction, reward])
            state=newstate
            
        G=0

        for x in reversed(history):
            G=j*G+x[2]
            #if seenStates[x[0]]==0:
            seenStates[x[0]]=1
            returns[x[0]]=returns[x[0]]+G
            n[x[0]]=n[x[0]]+1
            #stateValue[x[0]] = stateValue[x[0]] + stepSize*(returns[x[0]] - stateValue[x[0]])
            #elif seenStates[x[0]]==1:
             #   pass   
    #print(stateValue)
    stateValue=list(map(truediv,returns,n))    
    plt.plot(stateValue)
    
    recordStateValue.append(stateValue.copy())
    #recordStateValue = np.append(recordStateValue, stateValue)
    #print(recordStateValue)
   
#plt.plot(recordStateValue)
#plt.plot(stateValue)
plt.ylabel('State value')
plt.xlabel('State')
plt.title('Random walk')
plt.legend(['gamma=0.2', 'gamma=0.4', 'gamma=0.6', 'gamma=0.8', 'gamma=1'])
plt.show()
