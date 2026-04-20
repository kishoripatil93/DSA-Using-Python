#Lists
#lists are mutable and strings are immutable

marks = [89, 67, 54, 93, 45]
studentname = ["kk", "aa", "pk", "ll"]
print(marks)
print(type (marks))
print(marks[0], marks[2])
print(len(marks))
print(studentname)
print(type (studentname))
print(marks[0], studentname[2])
print(len(studentname))
studentname[2] = "oo"
print(studentname)

data = ["kp", 13, 90.87]
print(data)
print(len(data))

print(marks[:2])
print(marks[0:])
print(marks[3:])
print(marks[:-2])

#list methods
marks.append(37)
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(3, 70)
print(marks)

marks.remove(70)
print(marks)

marks.pop(4)
print(marks)

#practice 1
moviename = []
name = input("Favourite movie name 1: ")
moviename.append(name)
name = input("Favourite movie name 2: ")
moviename.append(name)
name = input("Favourite movie name 3: ")
moviename.append(name)
print(moviename)

#practice 2
list1 = [1, 'abc', 'abc', 1]
print(list1)
list2 = list1
list2.reverse()
print(list2)
if(list1 == list2):
    print("list is palindrom")
else:
    print("list is not palindrom")


#Tuple
#Tuple are immutable like strings

mark = (89, 67, 54, 93, 45)
studentname = ("kk", "aa", "pk", "ll")
print(mark)
print(mark.index(93))
print(type (mark))
empty = ()
print(empty)
print(type (empty))
print(mark[:2])
print(mark[0:])
print(mark[3:])
print(mark[:-2])

#practice 1
grade = ("C", "D", "A", "B", "A", "A", "A")
print(grade.count("A"))








