# Check if number is a 3-digit number or not take user input.
num = int(input("Enter a number: "))
if 100 <= abs(num) <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")
    

# Check if string length is greater than 5.
strr = input("Enter the string: ")
if len(strr) > 5:
    print(strr)
    print("string have 5 charactrer")
else:
    print("small strng")


# Check if number is zero so print ‘zero’ otherwise print ‘Not Zero’
num = int(input("Enter the no:"))
if(num == 0):
    print("Zero")
else:
    print("non-zero")



# Check if person can enter club (age + ID check). If yes, print ‘Eligible’.
age = int(input("Enter your age:"))
id = input("id checked or not write  yes/no")
if(age >=18 and id == 'yes'):
    print("Eligible")
else:
    print("not Eligible")


# Check if number is within range 10–50 if yes print ‘In Range’ otherwise ‘Not in Range’.
number = int(input("enter the no:"))
if(10>= number <=50):
    print("IN range")
else:
    print("Not in reange")    


# Simple calculator (+ or -) take both number and operator symbol from user.
no1 = eval(input("Enter the first no: "))
no2 = eval(input("Enter the second no: "))
add = no1+no2
sub = no1-no2
print("Your add is", add)
print("Your add is", sub)



# Check if username and password are correct if yes, print ‘Login Successful’.
username = input("Enter user_name: ")
passw = input("Enter your passowrd")
if(username == 'Aditya' and passw == '123ewq'):
    print("Login Successful") 
else:
    print("Invalid")


# Check if temperature is hot or cold.
temp = eval(input("Enter the temp: "))
if(temp > 25):
    print("hot")
else:
    print("cold")


# Check if number is palindrome (basic version) or not. If yes, print ‘Palindrome’ if no, print ‘Not Palindrome’.
nums = input("Enter the no: ")

if(nums == nums[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")


# Check if number is greater than 100.
num = int(input("Enter the no : "))
if(num > 100):
    print("yes")
else:
    print("no")



''' Q1. A bank provides loans based on the following conditions:
If the applicant's age is ≥ 21
If income is ≥ 25,000
If credit score is ≥ 700 → Loan Approved
Else → Loan Rejected (Low Credit Score)
Else → Loan Rejected (Low Income)
Else → Loan Rejected (Age not eligible)
Write a Python program using nested if statements to determine loan eligibility.'''

age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
score = int(input("Enter your credit score: "))
if age >= 21:
    if income >= 25000:
        if score >= 700:
            print("Eligible for loan")
        else:
            print("Low credit score")
    else:
        print("Low income")
else:
    print("Age not eligible")



''' Q2. Online Exam Result with Distinction
A student passes only if:
Marks in Maths ≥ 40
Marks in Science ≥ 40
Marks in English ≥ 40
If the student passes:
If average ≥ 75 → Distinction
Else → Pass
If any subject < 40 → Fail
Write a program using nested if to display result status.'''

math = int(input("Enter your math marks: "))
eng = int(input("Enter your eng marks: "))
sci = int(input("Enter your sci marks: "))
if math >= 40:
    if eng >= 40:
        if sci >= 40:
            if (math +sci + eng) / 3 >= 75:
                print("Distinction")
            else:
                print("Pass")
        else:
            print("Fail")
    else:
        print("Fail")
else:
    print("Fail")



''' Q3. Income Tax Calculator
A person pays tax based on:
If income > 5,00,000
If income ≤ 10,00,000 → 20% tax
Else → 30% tax
Else
If income > 2,50,000 → 5% tax
Else → No tax
Write a program using nested if to calculate tax amount.'''

income = int(input("Enter your income: "))
if income > 500000:
    if income < 1000000:
        print("20 % rax")
    else:
        print("30 % tax")
else:
    if income > 250000:
        print(" 5% tax")
    else:
        print("No tax")