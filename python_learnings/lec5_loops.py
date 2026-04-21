#while loops
count = 1  #iterators
while count <= 5:
    print("Hello")
    count += 1
    print(count)

print(count)

#practice 1
i = 1
while i <= 100:
    print(i)
    i += 1

#practice 2
i = 100
while i >= 1:
    print(i)
    i -= 1

#practice 3
list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
print(list1)

print(len(list1))
while i < len(list1):
    print(list1[i])
    i += 1

#practice 4
tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
x = 16
print(tup1)
print(len(tup1))

while i < len(tup1):
    if (x == tup1[i]):
        print("item fount at index", i)
        break
    i += 1
if (i == len(tup1)):
    print ("number not found")

#practice 5
print ("************* While loops: Practice question no 5 ***************")
n = 5
i = 0
sum = 0
while i <= 5:
    sum += i
    i += 1

print(sum)

#for loops
list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list2 = ["apple", "banana", "cat", "dog", "elephant"]
for num in list1:
    print(num)
for num in list2:
    print(num)

str = "abcdefghijklmnopqrstuvwxyz"
for char in str:
    print(char)

list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36
for num in list1:
    if (x == num):
        print(num, "found")
        break
    print("finding")

print(range(5))

for i in range(1, 10):
    print(i)

#odd  numbers
for i in range(1, 10, 2):
    print(i)

#even numbers
for i in range(2, 10, 2):
    print(i)

for i in range(10):
    print(i)

#practice 1
print ("*************Practice question no 1 ***************")
list1 = []
for i in range(1, 101):
    print(i)
    list1.append(i)
    
print ("*************Practice question no 2 ***************")
list1.reverse()
print(list1)
for num in list1:
    print(num)

for i in range(100, 0, -1):
    print(i)

print ("*************Practice question no 3 ***************")
num = int(input("Enter number"))
for i in range(1, 11):
    print(num * i)

print ("*************Practice question no 4 ***************")
num = int(input("Enter number"))
sum = 0
for i in range(num+1):
    sum += i
print(sum)

print ("************* Practice question no 5 ***************")
num = int(input("Enter number"))
fact = 1
for i in range(1, num+1):
    fact *= i

print(fact)

for i in range(5):
    pass

print("Pass statement is required to write some null statement")

