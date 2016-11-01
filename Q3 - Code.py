#Highest perfect square of a number

s = (int(input('Input number: ')))		    
x = 0						
if s >= 0:					
    while x*x < s: 					
        x +=1					
    if x*x != s: 					
        x=x-1					
        print(x)		
    else: print(x)
else: print(str(s)+ 'is not a positive number')
