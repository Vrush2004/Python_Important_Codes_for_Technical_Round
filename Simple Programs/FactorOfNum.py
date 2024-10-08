# Method 1 : Using [1, number] as the range
def printDivisors(n):
    i = 1
    while i<=0:
        if (n%i==0):
            print(i, end=" ")
        i = i+1
print("The divisors of 100 are : ")
printDivisors(100)

# Method 2: Using [1, sqrt(number)] as the Range
import math
def printDivisors(n):
    i = 1
    while i <= math.sqrt(n):
        if (n%i==0):
            if(n/i==i):
                print(i, end=" ")
            else:
                print(i, int(n/i), end=" ")
        i=i+1
print("The divisors of 100 are : ")
printDivisors(100)