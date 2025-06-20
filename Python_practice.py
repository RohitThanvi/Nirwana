""" If a number is divisible by 3 it should print “SKILLBREW”
 as a string
 If a number is divisible by 5 it should print “BRUDITE” as a
 string
 If a number is divisible by both 3 and 5 it should print
 “BRUDITE - NIRVANA” as a string
 """
a = int(input("Enter a number"))
 
if (a%3==0):
    print("SKILLBREW")
elif (a%5==0):
    print("BRUDITE")
elif (a%3 == 0 & a%5==0):
    print("BRUDITE - NIRVANA")
else:
    print("Invalid")
    
""" 2. Write a program that accepts a string as input from
 the user and calculates the number of digits and
 letters.
     Input: Hello123 
     Output: Alphabets: 5 & Number : 3"""
a=0
b=0    

str="Hello123"

for i in list(str):
    if i.isalpha():
        a += 1 
    elif i.isnumeric():
        b += 1
print(f"Total Alphabets {a}")
print(f"Total Numbers {b}")

"""3. Write a Python program to input marks for five
 subjects Physics, Chemistry, Biology, Mathematics,
 and Computer. Calculate the percentage and grade
 according to the following:
 Percentage >= 90% : Grade A
 Percentage >= 80% : Grade B
 Percentage >= 70% : Grade C
 Percentage >= 60% : Grade D
 Percentage >= 40% : Grade E
 Percentage < 40% : Grade F"""
 
Physics = float(input("Enter Marks in Physics"))
Chemistry = float(input("Enter Marks in Chemistry"))
Biology = float(input("Enter Marks in Biology"))
Mathematics = float(input("Enter Marks in Mathematics"))
Computer = float(input("Enter Marks in Computer"))

Percentage = (Physics + Chemistry + Biology + Mathematics + Computer)/5

if(Percentage>=90.0):
    print("Grade A")
elif(Percentage>=80.0):
    print("Grade B")
elif(Percentage>=70.0):
    print("Grade C")
elif(Percentage>=60.0):
    print("Grade D")
elif(Percentage>=40.0):
    print("Grade E")
elif(Percentage<40.0):
    print("Grade F")
else:
    print("Invalid")

""" Write a Python program to find the sum of all odd
 numbers between two given numbers."""
i=1
sum=0
while(i<11):
    sum = sum + i
    i=i+2
print(f"sum {sum}")

"""Write a Python program to find the factorial of a
 number using a for loop"""
 
fact = 1
a=10
i=1
while(i<=a):
    fact=fact*i
    i += 1
print(fact)

"""6. Write a Python program to check if a given number
 is a perfect number. """

num = int(input("Enter a number: "))
total = 0
for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print("Yes")
else:
    print("No")
    
"""7. Write a Python program to check if a string is an
 anagram of another string."""

a = input("Enter first string: ")
b = input("Enter second string: ")

if sorted(a) == sorted(b):
    print("True")
else:
    print("False")

""" Write a Python program to calculate the LCM (Least
 Common Multiple) of two numbers."""

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    big = x
else:
    big = y

while True:
    if big % x == 0 and big % y == 0:
        print("LCM is:", big)
        break
    big += 1
    
"""Write a Python program to count the frequency of
 each element in a list."""

lst = [1, 2, 3, 2, 4, 1, 2, 4, 5]
freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

""" 10. Write a Python program to reverse the order of
 words in a given sentence."""

s = input("Enter a sentence: ")
words = s.split()
reversed_words = words[::-1]
result = " ".join(reversed_words)
print(result)

"""11. Write a Python program to calculate the sum of
 digits of a given number until the sum becomes a
 single-digit number."""

num = int(input("Enter a number: "))

def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

while num > 9:
    num = sum_digits(num)

print("Final Output:", num)

"""12. Write a Python program to reverse a number using
 a while loop."""

num = int(input("Enter a number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print("Reversed number is:", rev)
