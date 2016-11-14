#Binary search to output whether a value within a specific interval was found

def binarySearch(alist,low,high,n):
    start = 0
    end = n
    mid = 0

    while start < end:
        mid = int(start + (end-start)/2) #Locate middle of array

        if (low > alist[mid]) and (high > alist[mid]): #Check if low number is > mid number and if high number > mid number
            start = mid+1 #New start of list is mid + 1

        elif (low < alist[mid]) and (high < alist[mid]): #Check if low number is < mid number and if low number < mid number
            end = mid #New end of list is mid

        else:
            return True

    return False

print('List: [2,3,5,7,9,13]')
alist = [2,3,5,7,9,13]
n = 6
low = int(input('Enter low: '))
high = int(input('Enter high: '))
print(binarySearch(alist,low,high,n))
