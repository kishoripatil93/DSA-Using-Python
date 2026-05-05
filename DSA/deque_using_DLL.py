class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.rear == None
    
    def insert_first(self, data):
        n = Node(data, None, self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.item_count += 1

    def insert_last(self, data):
        n = Node(data, self.rear)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n  
        self.item_count += 1   

    def delete_first(self):
        if self.is_empty():
            return

        if self.front == self.rear:
            temp = self.front            
            self.front = None
            self.rear = None
            self.item_count -= 1 
            return temp.data
            
        else:
            temp = self.front
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1 
        return temp.data
    
    def delete_last(self):
        if self.is_empty():
            return

        if self.front == self.rear:
            temp = self.rear
            self.front = None
            self.rear = None
            self.item_count -= 1 
            return temp.data
        else:
            temp = self.rear
            self.rear = self.rear.prev
            self.rear.next = None
            self.item_count -= 1 
            return temp.data
               
    def print_list_elt(self):
        temp = self.front
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next
        print()
        temp = self.rear
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.prev
        print()

    def get_item_count(self):
        return self.item_count
    
    def get_front(self):
        if self.is_empty():
            return
        return self.front.data
    
    def get_rear(self):
        if self.is_empty():
            return
        return self.rear.data

d1 = Deque()
d1.insert_first(10)
d1.insert_first(20)
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

d1.insert_last(30)
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

d1.insert_last(40)
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

print("\ndeleted first item = ", d1.delete_first())
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

print("\ndeleted last item = ", d1.delete_last())
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

print("\ndeleted first item = ", d1.delete_first())
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

print("\ndeleted first item = ", d1.delete_first())
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

print("\ndeleted last item = ", d1.delete_last())
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

print("\ndeleted first item = ", d1.delete_first())
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

d1.insert_first(85)
d1.insert_last(87)
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())

d1.insert_first(81)
d1.insert_last(90)
d1.print_list_elt()
print("item count is = ", d1.get_item_count())
print("Front = ", d1.get_front(), "rear = ", d1.get_rear())