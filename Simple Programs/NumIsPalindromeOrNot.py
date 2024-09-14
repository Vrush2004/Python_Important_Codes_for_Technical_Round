# Method 1:  Using Simple Iteration.
num = 1221
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
    print("Palindrome")
else:
    print("Not palindrome")

# Method 2: Using String Slicing
num = 1234
reverse = int(str(num)[::-1])
if num == reverse:
    print("Palindrome")
else:
    print("Not palindrome")

# Method 3: Using Recursion
def recurrev(number, rev):
    if number == 0:
        return rev
    remainder = int(number % 10)
    rev = (rev * 10) + remainder
    return recurrev(int(number/10), rev)
num = 12321
reverse = 0
reverse = recurrev(num, reverse)
print(str(num) + " is: ", end="")
print("Palindrome") if reverse == num else print("Not palindrome")

# Method 4: Using Character matching
def checkPalindrome(str):
    for i in range(0, len(str)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
s = "nayan"
print("Palindrome") if checkPalindrome(s) else("Not palindrome")

# Method 5: Using Character matching (Updated)
def checkPalindrome(str):
    mid = int(len(str) / 2)
    for i in range(0, mid):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
s = "nayan"
print("Palindrome") if checkPalindrome(s) else("Not palindrome")

# Method 6: Using In-Built reversed function
def checkPalindrome(str):
    reverse = ''.join(reversed(str))
    if str == reverse:
        return True
    return False
s = "nayan"
print("Palindrome") if checkPalindrome(s) else("Not palindrome")

# Method 7: Building reverse one char at a time
string = "123"
rev = ''
for char in string:
    rev = char + rev
print("Palindrome") if str == rev else print("Not Palindrome")

print("string: " + str(string))
print("rev: " + str(rev))

# Method 8: Using Flag
string = "radar"
j = -1
flag = 0
for char in string:
    if char != string[j]:
        flag = 1
        break
    j = j-1
print(string + " is : ", end="")
print("Not Palindrome") if flag else print("Palindrome")

# Method 8: Bonus using backward slicing
str1 = "radar"
n = len(str1)
c = []
for i in range(n-1, -1, -1):
    c.append(str1[i])
rev = "".join(c)

print(str1 + " is: ", end="")
if str1 == rev:
    print("Palindrome")
else:
    print("Not Palindrome")