#Longest increasing subsequence

sequence = [1,2,3,4,1,5,1,6,7]
longest_first = -1
length = 0
longest_length = 0


for i in range(len(sequence)):
    if (i + 1 == len(sequence)): #Check if its the end of the array
        if (length > longest_length):
            longest_length = length
            longest_first = i - longest_length
            break
        
    elif (sequence[i] < sequence[i + 1]): #Check if index is smaller than the next index
        length += 1

    elif (length >= longest_length): #Check if length is longer than longest to change the length
        longest_length = length
        longest_first = i - length #Longest is changed to first to see where to start from
        length = 0

for i in range(longest_first, longest_first + longest_length+1):
    print(sequence[i])
