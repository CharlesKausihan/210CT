#Highest perfect square of a number

def highestPerfectSquare(s):
    x = 0
    if s >= 0:
        while x*x < s:
            x +=1 #Keep adding 1 to x
        if x*x != s:
            x=x-1 #Take 1 away from x if x*x is bigger than s
            print(x)
        else: print(x)
    else: print(str(s)+' is not a positive number')

s = (int(input('Input number: ')))
print(highestPerfectSquare(s))
