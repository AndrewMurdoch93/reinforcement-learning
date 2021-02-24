import numpy as np
from agent import random_policy
import matplotlib.pyplot as plt
from operator import truediv
from operator import itemgetter, attrgetter

#returns=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#stateValue=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#recordStateValue=[]
#gamma=[0.2, 0.4, 0.6, 0.8, 1]
gamma=1
#seenStates=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#stepSize=0.1
#n=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
reward=[]
state_action_pairs=[]

#for j in gamma:
    #for y in range(500):
state=0
#seenStates=[0,0,0,0,0,0,0,0,0,0]
history=[]
t=0
#returns=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while state<10:
    t=t+1
    direction = random_policy()
    
    if [state, direction] not in state_action_pairs:
        state_action_pairs.append([state, direction].copy())

    if direction == 'l':
        newstate = state-1
    elif direction == 'r':
        newstate = state+1

    if newstate<0:
        newstate=0

    if newstate==10:
        newReward=0
    elif newstate!=10:
        newReward=-1

    history.append([state, direction])
    reward.append(newReward)
    state=newstate

G=0
returns = [0]*len(state_action_pairs)
n = [0]*len(state_action_pairs)
returns = [0]*len(state_action_pairs)
state_action_pairs = sorted(state_action_pairs, key=itemgetter(0,1), reverse=False)


for x in reversed(history):
    t=t-1
    G=gamma*G+reward[t]
    index=state_action_pairs.index(x)
    #if seenStates[x[0]]==0:
    #seenStates[x[0]]=1
    returns[index]=returns[index]+G
    n[index]=n[index]+1
    #stateValue[x[0]] = stateValue[x[0]] + stepSize*(returns[x[0]] - stateValue[x[0]])
    #elif seenStates[x[0]]==1:
        #   pass   
#print(stateValue)

newlist=[]
stateValue=list(map(truediv,returns,n))    
pass
print(stateValue)
for x in state_action_pairs:
    if "l" in x:
        newlist.append(x)

newlist = [x for x in state_action_pairs if "l" in x]
pass
#plt.plot(stateValue)

#recordStateValue.append(stateValue.copy())
#recordStateValue = np.append(recordStateValue, stateValue)
#print(recordStateValue)

#plt.plot(recordStateValue)
#plt.plot(stateValue)
#plt.ylabel('State value')
#plt.xlabel('State')
#plt.title('Random walk')
#plt.legend(['gamma=0.2', 'gamma=0.4', 'gamma=0.6', 'gamma=0.8', 'gamma=1'])
#plt.show()
