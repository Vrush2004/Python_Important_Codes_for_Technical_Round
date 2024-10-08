# Method 1: Using Simple Iteration
n = 145
temp = n
sum = 0
f = [0]*10
f[0]=1
f[1]=1
for i in range(2,10):
    f[i] = f[i-1]*i

while (temp):
    r=temp%10
    temp=temp
    sum+=f[r]

if(sum == n):
    print("Yes", n, "is strong number")
else:
    print("No", n, "is not a strong number")

# Method 2: Using Recursive Function
def Factorial(num):
    if num<=0: 
        return 1 
    else: 
        return num*Factorial(num-1)
     
sum=0 
def check_StrongNumber(num): 
    global sum 
    if (num>0):
        fact = 1
        rem = num % 10
        check_StrongNumber(num//10)
        fact = Factorial(rem)
        sum+=Factorial
    return sum
num = 145
if(check_StrongNumber == num):
    print("Yes", num, "is strong number")
else:
    print("No", num, "is not a strong number")