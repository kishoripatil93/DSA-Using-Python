class stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0
    
    def push(self, item):
        self.list.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.list.pop()
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")

        return self.list[-1]
    
    def size(self):
        return len(self.list)
    
myStack = stack()
myStack.push(9)
myStack.push(6)
myStack.push(2)
for x in myStack.list:
    print(x)
print("size", myStack.size())
print("popped", myStack.pop())
for x in myStack.list:
    print(x, end=" ")
print("size", myStack.size())
print("peek", myStack.peek())
