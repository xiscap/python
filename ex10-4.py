"""
pedra=0
paper=1
tisores=2
"""
y=int(input("Digués pedra=0, paper=1 o tisores=2: " ))

import random
x = ["0", "1", "2"]
random_index = random.randrange(0,3)
print(x[random_index])

#print(x)
if (x == 0 and y == 1) or (x == 1 and y == 2) or (x == 2 and y == 0):
    print("Has guanyat!")
elif (x == 0 and y == 2) or (x == 1 and y == 0) or (x == 2 and y == 1):
    print("Has perdut")
else:
    print("Has empatat")