import random

def random_policy():
    random.seed()
    direction = random.uniform(0,1)
    
    if direction>0.5:
        return 'r'
    elif direction<=0.5:
        return 'l'





