#Longest increasing subsequence

sequence = [1,2,3,4,1,5,1,6,7]
longestFirst = -1
length = 0
longestLength = 0

#Check if element in higher or lower than the last element
for i in range(len(sequence)):
    if (i + 1 == len(sequence)): #Check if it is at the end of the array
        if (length > longestLength): 
            longestLength = length
            longestFirst = i - longestLength
            break
        
    elif (sequence[i] < sequence[i + 1]): #Check if elements is smaller than the next elements
        length += 1

    elif (length >= longestLength): #Check if length is bigger than longestLength to change the length
        longestLength = length
        longestFirst = i - length #Longest is changed to first to see where to start from
        length = 0

for i in range(longestFirst, longestFirst + longestLength+1):
    print(sequence[i])
