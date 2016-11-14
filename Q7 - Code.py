#Check if a number is a prime

n = int(input("Enter a number: "))

if n > 1: #prime numbers are greater than 1
    for i in range(2,n): #numbers from 2 to n-1
       if (n % i) == 0: #check if dividing n by numbers from 2 to n-1 gives remainder
           print(n,"is not a prime number")
           break

    else:
        print(n,"is a prime number")
       
else:
    print(n,"is not a prime number")
