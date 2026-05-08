def sum_of_n_numbers(n):
    if n == 1:
        return 1
    s = n + sum_of_n_numbers(n - 1)
    return s

print(sum_of_n_numbers(3))
print(sum_of_n_numbers(4))
print(sum_of_n_numbers(100))

def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=" ")

printN(10)
print()

def printNR(n):
    if n > 0:
        print(n, end=" ")
        printNR(n - 1)
printNR(10)
print()

def print_odd(n):
    if n > 0:
        print_odd(n - 1)
        print(2*n - 1, end=" ")
print_odd(10)
print()
    
def print_even(n):
    if n > 0:
        print_even(n - 1)
        print(2*n, end=" ")
print_even(10)
print()

def print_odd_R(n):
    if n > 0:
        print(2*n - 1, end=" ")
        print_odd_R(n - 1)
        
print_odd_R(3)
print()
    
def print_even_R(n):
    if n > 0:
        print(2*n, end=" ")
        print_even_R(n - 1)
        
print_even_R(3)
print()

def sum_odd_N_num(n):
    if n <= 0:
        return 0
    s = 2*n - 1 + sum_odd_N_num(n - 1)
    return s

print(sum_odd_N_num(3))

def sum_even_N_num(n):
    if n <= 0:
        return 0
    s = 2*n + sum_even_N_num(n - 1)
    return s

print(sum_even_N_num(3))

def fact(n):
    if n == 0 or n == 1:
        return 1
    f = n * fact(n-1)
    return f
print(fact(3))

print(fact(4))

def sum_square_N_num(n):
    if n == 1:
        return 1
    s = n*n + sum_square_N_num(n - 1)
    return s

print(sum_square_N_num(3))