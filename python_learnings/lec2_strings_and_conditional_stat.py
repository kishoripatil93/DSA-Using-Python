name = input("Enter your name ")
surname = input("Enter your surname ")
full_name = name +  " " + surname
print("Coplete name", full_name)
str1 = "This is pleasanton"
str2 = '422004'
print(len(str1))
print(str1[0])
#str1[0] = 't'   // Error TypeError: 'str' object does not support item assignment

print(str1[0:3])  # excludes last index char
print(str1[8:])
print(str1[:7])
print(str1[:-10])
print(str1.endswith("ton"))
print(str1.capitalize())
print(str1.replace("pleasanton", "milpitas"))
print(str1.find("pleasanton"))
print(str1.count('i'))

# Practice 1
name = input("Enter your name");
print("lenghth of name is", len(name))

#conditional statements
age = 20

if (age >= 21):
    print("Can vote")
    print("Can drive")
else:
    print("Not eligible to vote and drive")




