# Method 1: Using Brute Force
num = 15
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Given Number is zero")

# Method 2: Using Nested if-else Statements
num = 15
if num >= 0:
    if num==0:
        print("Given Number is zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")

# Method 3: Using Ternary Operator
num = 15
print("Positive" if num>=0 else "Negative")