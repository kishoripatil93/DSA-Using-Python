f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))

line1 = f.readline()
print(line1)
f.close()

with  open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("We are learning file  I/O\n")
    f.write("using Java.\n")
    f.write("I like programming in Java.\n")

with open("practice.txt", "r") as f:
    data = f.read()

print(data.find("learning"))
if (-1 != data.find("learning")):
    print("Word present")
else:
    print("Not find")

new_data = data.replace("Java", "Python")

with  open("practice.txt", "w") as f:
    f.write(new_data)

word = "learning"
line = True
line_no = 0
with  open("practice.txt", "r") as f:
    while line:
        line = f.readline()
        print(line)
        line_no += 1
        if (word in line):
            print("word found at line no ", line_no)
            break

with open("evenno.txt", "w") as f:
    f.write("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

with open("evenno.txt", "r") as f:
    data = f.read()
    print(data)
    num = data.split(",")
    value = 0
    print(num)
    for values in num:
        if((int(values) % 2 )== 0):
            print(values)    
