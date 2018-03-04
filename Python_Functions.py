
#import matplotlib.pyplot as plt
#plt.plot(x,y) or plt.scatter(), plt.hist(), plt.show(), to clear plot plt.clf()
#to change scale plt.xscale('log')
#plt.xlabel(''), plt.ylabel(''),plt.title(''),plt.yticks([2,4,6,8],[label1,label2,label3])

#dictionaries: world={'afghanistan':3, 'albania':4, 'algeria':4} dictionaries['albania']
#for adding values: world['turkey]=5, for removing values del(world['turkey'])

#import pandas as pd, cars=pd.read_csv('cars.csv')

#loc and iloc. cars.loc: labels, cars.iloc, indexes

#np.locial_and(x,y)

z=6 
if z%2==0:
    print("z is divisible by 2")
elif z%3==0:
    print("z is divisible by 3")
else:
    print("z is neither divisible  by 2 or 3")
    
x=1
while x < 4:
    print(x)
    x = x + 1
    
fam=[1,2,3,4]
for x in fam:
    print(x)
    
fam=[1,2,3,4]
for index, x in enumerate(fam):
    print("index " + str(index) + ": " + str(x) )

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x in house:
    print("the " + x[0] + " is " + str(x[1]) + " sqm")
    
#for dictionary: for key, value in my_dict.items()
# for np array: for val in np.nditer(my_array)
    
import numpy as np
np.random.seed(123)
outcomes=[]
for x in range(10):
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print(outcomes)   
