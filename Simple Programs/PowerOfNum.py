# Method 1: Using Pow() Function
num, power =3,2
print(pow(num,power))

# Method 2: Using Simple Iteration
num, power =3,2
output = 1
for i in range(power):
    output*=num
print(output)

# Method 3: Using Python Operator
num, power =3,2
print(num**power)

# Method 4: Using Recursion
num, power =3,2
def powerrecur(num, power):
    if power == 0:
        return 1
    return num * powerrecur(num, power-1)
print(powerrecur(num, power))