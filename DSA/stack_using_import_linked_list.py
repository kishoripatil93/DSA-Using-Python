from singly_linked_list import *

class stack:
    def __init__(self, item_count = 0):
        self.myList = SLL()
        self.item_count = item_count

    def is_empty(self):
        return self.myList.is_empty()
    
    def push(self, data):
        self.myList.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.myList.is_empty():
            self.myList.del_first_elt_in_list()
            self.item_count -= 1

    def print_stack(self):
        self.myList.print_list_elt()

    def peek (self):
        if not self.myList.is_empty():
            return self.myList.start.item
        
    def size(self):
        return self.item_count

s1 = stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
s1.print_stack()
s1.pop()
s1.print_stack()
print(s1.peek())
print(s1.size())
