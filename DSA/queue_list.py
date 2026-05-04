class Queue:
    def __init__(self):
        self.myQueue = []
        
    def is_empty(self):
        return len(self.myQueue) == 0
    
    def enqueue(self, data):
        self.myQueue.append(data)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            self.myQueue.pop(0)

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.myQueue[-1]
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.myQueue[0]
    
    def get_size(self):
        return len(self.myQueue)

q1 = Queue()
print("size =", q1.get_size())

q1.enqueue(10)
print("front =", q1.get_front())
print("rear =", q1.get_rear())
print("size =", q1.get_size())

q1.enqueue(20)
print("front =", q1.get_front())
print("rear =", q1.get_rear())
for x in q1.myQueue:
    print(x, end= " ")
print()
print("size =", q1.get_size())

q1.dequeue()
print("front =", q1.get_front())
print("rear =", q1.get_rear())
for x in q1.myQueue:
    print(x, end= " ")
print()
print("size =", q1.get_size())

q1.enqueue(30)
print("front =", q1.get_front())
print("rear =", q1.get_rear())
for x in q1.myQueue:
    print(x, end= " ")
print()
print("size =", q1.get_size())

q1.enqueue(40)
print("front =", q1.get_front())
print("rear =", q1.get_rear())
for x in q1.myQueue:
    print(x, end= " ")
print()
print("size =", q1.get_size())

q1.dequeue()
print("front =", q1.get_front())
print("rear =", q1.get_rear())
for x in q1.myQueue:
    print(x, end= " ")
print()
print("size =", q1.get_size())