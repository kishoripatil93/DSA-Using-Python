print("Hello World", "My name is Naina", 12345, 2 + 3, "Next")
age = 20.999
age2 = age
print (age2)
age = "bunny"
print (type (age))
print (type (age2))

a = 5
b = 2

# Arithmetic
print("Arithemetic")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#logical
print("Logical")
print(a and b)
print(a or b)
print (not (a > b))

# Rational operator
print("Rational")
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

#type conversion
a = 4.5
sum = a + b
print(sum)

#type conversion -> Error
#a = "4.5"
#sum = a + b
#print(sum)

#type casting 
a = float("4.5")
sum = a + b
print(sum)

#Input from user
name = input("Enter your name: ")
print ("Welcome", name)

num = input("Enter your number: ")
print ("You entered", num)
print (type(num))

num = int(input("Enter your number: "))
print ("You entered", num)
print (type(num))

#exercise 1
num1 = int(input("Enter 1st number: "))
print ("You entered", num1)
num2 = int(input("Enter 2nd number: "))
print ("You entered", num2)
print (type(num))
print ("Sum of two numbers is : ", num1 + num2)

#execise 2
side = float(input("Enter side of square: "))
print("Area of square is: ", side * side)

#exercise 3
num1 = float(input("Enter 1st number: "))
print ("You entered", num1)
num2 = float(input("Enter 2nd number: "))
print ("You entered", num2)
print("Average of two float numbers is: ", ((num1 + num2) / 2))