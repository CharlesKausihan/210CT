#Randomising an array

import random
array = [5,3,8,6,1,9,2,7]
newArray = []

def Random(a):
    while array!=[]: #Array isn't empty
        x = random.randrange(len(array)) #Picks random number from range of array
        newArray.append(array[x]) #Gets element from randomly picked place value and adds to newArray from array
        del array[x] #Deletes array
    
Random(array)
print(newArray)
