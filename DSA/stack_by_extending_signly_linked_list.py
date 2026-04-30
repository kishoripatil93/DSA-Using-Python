from singly_linked_list import *
class stack(SLL):
    def __init__(self, item_count=0):
        super().__init__()
        self.item_count = item_count

    def is_empty(self):
        return super().is_empty()
    
    def push(self, data):
        self.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.del_first_elt_in_list()
            self.item_count -= 1
        else:
            raise IndexError("empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("empty stack")
        
    def size(self):
        return self.item_count
    

s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
s1.pop()
print(s1.peek())