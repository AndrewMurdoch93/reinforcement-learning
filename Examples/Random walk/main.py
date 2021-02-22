import numpy as np
from agent import random_policy

state=1
returns=np.array([0, 0, 0, 0, 0])
history=[]
G=0
t=0
gamma=0.9

while state<5:
    t=t+1
    direction = random_policy()

    if direction == 'l':
        newstate = state-1
    elif direction == 'r':
        newstate = state+1

    if newstate<1:
        newstate=1

    if state==5:
        reward=1
    elif state!=5:
        reward=0

    history.append([state, direction, reward])
    state=newstate
    
for x in range(t, 1):
    print(history[x][1])
