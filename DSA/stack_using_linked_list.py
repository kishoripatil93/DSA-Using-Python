class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class stack:
    def __init__(self, start = None, item_count = 0):
        self.start = start
        self.item_count = item_count

    def is_empty(self):
        return self.start == None
    
    def push(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else: 
            val = self.start.val
            self.start = self.start.next
            self.item_count -= 1
            return val

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else: 
            return self.start.val

    def size(self):
        return self.item_count

    def print_stack(self):
        temp = self.start
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()

myStack = stack()
myStack.push(1)
myStack.push(2)
myStack.print_stack()
print("popped", myStack.pop())
myStack.print_stack()
myStack.push(3)
myStack.print_stack()
myStack.push(4)
myStack.push(5)
myStack.push(6)
myStack.print_stack()
print("top elt is", myStack.peek())
print("size is", myStack.size())