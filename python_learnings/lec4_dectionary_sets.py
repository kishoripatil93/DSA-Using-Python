#Dictinaries
#Dictinary is mutable, unordered, don,t allow duplicate keys

info = {
    "name" : "kp",
    "age" : 20,
    "weight": 50.54,
    "subjects":["python", "c", "c++"],
    "topics":("dictionary", "sets"),
    "is_adult": False
}
print(info)
print(type(info))
print(info["name"])
info["name"] = "pp"
print(info)

#methos
print(list(info.keys()))
print(len(list(info.keys())))

print(list(info.values()))
print(len(list(info.values())))

print(list(info.items()))
print(len(list(info.items())))

print((info.get("name")))

#practice 1
dict1 = {
    "table": ["A piece of furniture", "list of facts or figure "],
    "cat": "a small animal"
}

print(dict1)

#practice 2
dict2 = {}
subject = input("Enter the subject as key")
marks = float(input("enter marks as value"))
dict2[subject] = marks

subject = input("Enter the subject as key")
marks = float(input("enter marks as value"))
dict2[subject] = marks

subject = input("Enter the subject as key")
marks = float(input("enter marks as value"))
dict2[subject] = marks

print(dict2)


#sets
#is  collection of unique and immutable elts 
#set os unordered elts

#sets are mutable but elts in this are immutable

collection = {1, 2, 3, 4, 5, "hello", 5}
print(collection)
print(type(collection))
print(len(collection))

empty_set = set() # not just {}

collection.add(6)
print(collection)
collection.remove(1)
print(collection)
collection.pop()
print(collection)

#collection.add([7, 8, 9])  # error as lists are mutable

collection2 = {5, 6, 7, 8}
print(collection.union(collection2))
print(collection.intersection(collection2))
collection.clear()
print(collection)

#practice 1
subjects = {"python", "c++", "c", "java", "python", "python", "c++", "c", "java", "python"}
print(len(subjects))

#practice 2

set1 = {9, "9.0"}
print(set1)
