# Method 1 : Using Brute Force
num = int(input("Enter a number: "))
if num % 2 ==0:
    print("Number is Even")
else:
    print("Number is Odd")

# Method 2 : Using Ternary Operator
num = 17
print("even") if num%2 == 0 else print("Odd")

# Method 3 : Using Bitwise Operator
def isEven(num):
    return not num&1

if __name__ == "__main__" :
    num = 13
    if isEven(num):
        print("even")
    else:
        print("Odd")