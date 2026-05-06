class Node:
    def __init__(self, data = None, priority = None, next = None):
        self.data = data
        self.priority = priority
        self.next = next

class PriorityQ:
    def __init__(self, start = None):
        self.start = start
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self, data, priority):
        n = Node(data, priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next

            n.next = temp.next
            temp.next = n
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            return
        temp = self.start.data
        self.start = self.start.next
        self.item_count -= 1
        return temp
    
    def get_item_count(self):
        return self.item_count
        
    def print_elt(self):
        if self.is_empty():
            return        
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.next
        print("\n")

p1 = PriorityQ()
p1.push("Bapurao", 1)
p1.push("Mukesh", 4)
p1.push("kishori", 5)
p1.push("Omkar", 6)
p1.push("Meenakshi", 2)
p1.push("Deepak", 3)
p1.push("DumDum", 0)
print("item count is ", p1.get_item_count())
p1.print_elt()

print("popped = ",p1.pop(), "\n")
p1.print_elt()

while not p1.is_empty():
    print(p1.pop())