class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class Queue:
    def __init__(self, front = None, rear = None, item_count = 0):
        self.front = front
        self.rear = rear
        self.item_count = item_count

    def is_empty(self):
        return self.front == None
    
    def enqueue(self, data):
        n = Node(data, None)
        if self.front == None:
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            return

        temp = self.front.data
        self.front = self.front.next
        self.item_count -= 1
        return temp
    
    def get_front(self):
        if not self.is_empty():
            return self.front.data
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
    
    def get_item_count(self):
        return self.item_count
    
    def print_elt(self):
        temp = self.front
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()


q1 = Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.print_elt()
print("\nfront is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())

print("\ndeleted item = ",  q1.dequeue())
q1.print_elt()
print("front is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())

q1.enqueue(50)
q1.print_elt()
print("\nfront is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())


print("\ndeleted item = ",  q1.dequeue())
q1.print_elt()
print("front is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())

print("\ndeleted item = ",  q1.dequeue())
q1.print_elt()
print("front is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())

print("\ndeleted item = ",  q1.dequeue())
q1.print_elt()
print("front is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())

print("\ndeleted item = ",  q1.dequeue())
q1.print_elt()
print("front is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())
    
    
print("\ndeleted item = ",  q1.dequeue())
q1.print_elt()
print("front is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())
    
    
q1.enqueue(70)
q1.print_elt()
print("\nfront is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())

print("\ndeleted item = ",  q1.dequeue())
q1.print_elt()
print("front is ", q1.get_front())
print("rear is ", q1.get_rear())
print("item_count is ", q1.get_item_count())