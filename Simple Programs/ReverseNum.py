# Method 1: Using Simple Iteration
num = 1234
temp = num
reverse = 0
while num>0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
print(reverse)

# Method 2: Using String Slicing
num = 1234
print(str(num)[::-1])

# Method 3: Using Recursion
def recursum(number, reverse):
    if number == 0:
        return reverse
    remainder = int(number%10)
    reverse = (reverse*10) + remainder
    return recursum(int(number/10), reverse)
num=1234
reverse=0
print(recursum(num, reverse))