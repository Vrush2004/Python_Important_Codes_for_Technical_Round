# Method 1: Using Simple Iteration
num = 10
n1,n2 = 0,1
print("Fibonacci Series: ", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()

# Method 2: Using Recursive Function
def fibonacciSeries(i):
    # Correct base cases
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacciSeries(i-1) + fibonacciSeries(i-2)

num = 10  # Number of terms to generate
if num <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci Series:", end=" ")

for i in range(num):
    print(fibonacciSeries(i), end=" ")
