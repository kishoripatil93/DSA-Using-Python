#OOPS concepts
#class is blueprint of objects
class Student:
    college = "PVG"  # class Attributes this is stored only once in memory 
    #default constructors
    def __init__(self):
        pass
    
    #parameterised constructors
    def __init__(self, name, marks):
        self.name = name    #object attribute
        self.marks = marks
        print("Adding student in database")

    def hello(self):
        print("Welcome student", self.name)

    def get_marks(self):
        print("marks = ", self.marks)

s1 = Student("kk", 90)
print(s1.name)
print(s1.marks)
print(s1.college)
s1.hello()
s1.get_marks()
s2 = Student("oo", 91)
print(s2.name)
print(s2.marks)

class Car:
    colour = "blue"
    brand = "mercedez"

c1 = Car()
print(c1.brand)
print(c1.colour)

print ("************* Practice question no 1 ***************")
class Student1:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_average(self):
        avg = 0
        avg = (self.marks[0] + self.marks[1] + self.marks[2]) / 3
        print("Hi ", self.name, "your avg marks are = ", avg)


marks = [80, 85, 90]
s1 = Student1("tony stark", marks)
s1.get_average()

print ("************* Practice question no 2 ***************")
class Account:
    def __init__(self, acc_balance, acc_no, acc_pass):
        self.acc_balance = acc_balance
        self.acc_no = acc_no
        self.__acc_pass = acc_pass    #private attributes

    def debit(self):
        debitamount = float(input("how much you want to debit"))
        print("Rs ", debitamount, "is debited to your account")
        self.acc_balance -= debitamount
        print("After debit your balance is ", self.acc_balance)

    def credit(self):
        creditamount = float(input("how much you want to credit"))
        print("Rs ", creditamount, "is credited to your account")
        self.acc_balance += creditamount
        print("After credit your balance is ", self.acc_balance)

    def print_balace(self):
        print("After credit your balance is ", self.acc_balance)

a1 = Account(4000, 12345678, "abc")
print(a1.acc_no)
a1.debit()
a1.credit()
a1.print_balace()

#private attributes
class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello")

    def welcome(self):
        self.__hello()

p1 = Person()
p1.welcome()

#Inheritance single and multilevel
class Car:
    @staticmethod
    def start():
        print("Engine started")

    @staticmethod
    def stop():
        print("Engine stpped")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
    

car1 = Fortuner("diesel")
car1.start()


#multiple inheritance
class A:
    vara = "This is car A"

class B:
    varb = "This is car B"

class C(A, B):
    varc = "This is car C"

c1 = C()
print(c1.vara)
print(c1.varb)
print(c1.varc)

#Super Method