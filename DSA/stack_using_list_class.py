class stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self, data):
        self.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return super().pop()
        
    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return self[-1]  

    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("No attribute insert in stack")


s1 = stack()   
s1.push(10)  
s1.push(20)  
s1.push(30) 
for x in s1:
    print(x, end=" ")
print()
print(s1.peek())
print(s1.pop())
print(s1.size())

