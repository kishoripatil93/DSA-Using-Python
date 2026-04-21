# Functions
def calc_sum (a, b):
    return a + b

def print_hello ():
    print("Hello")

def calc_average(a, b, c):
    return((a+b+c)/3)

def calc_prod(a, b = 2):
    return a * b


a = 5
b = 10
print(calc_sum(a, b))
print_hello()
print(calc_average(2,4,7))
print(calc_prod(3))

print("****************** Practice question 1 **************")
list1 = [89, 67, 54, 93, 45]
def print_list_len(a):
    print(len(a))

print_list_len(list1)

print("****************** Practice question 2 **************")
def print_list_elt(a):
    for elt in a:
        print(elt, end=" ")
    print()

print_list_elt(list1)

print("****************** Practice question 3 **************")
def fact_num(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(fact_num(5))

print("****************** Practice question 4 **************")
def USD_to_INR(n):
    return n * 92.74

print(USD_to_INR(50))


#Recursion
def show(n):
    if(n == 0):
        return
    print(n)
    show(n - 1)

show(5)

print("****************** Practice question 1 **************")
def recursive_fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * recursive_fact(n - 1)

print(recursive_fact(5))

print("****************** Practice question 2 **************")
def recursive_sum(n):
    if (n == 0):
        return 0
    return n + recursive_sum(n - 1)

print(recursive_sum(5))

print("****************** Practice question 3 **************")
def recursive_print_list_elt(list1, index):
    if (index == len(list1)):
        return
    print(list1[index], end = " ")
    recursive_print_list_elt(list1, index + 1)

list1 = [89, 67, 54, 93, 45]
recursive_print_list_elt(list1, 0)
print()