class PriorityQ:
    def __init__(self):
        self.list = []
    
    def is_empty(self):
        return len(self.list) == 0
    
    def push(self, data, priority):
        index = 0
        while index < len(self.list) and self.list[index][1] <= priority:
            index += 1

        self.list.insert(index, (data, priority))

    def pop(self):
        if self.is_empty():
            return
        return self.list.pop(0)[0]
    
    def size(self):
        return len(self.list)


p1 = PriorityQ()
p1.push("kishori", 4)
p1.push("omkar", 2)
for x in p1.list:
    print(x, end=" ")
print()

p1.push("weds", 1)
for x in p1.list:
    print(x, end=" ")
print()
print("size = ", p1.size())

print("popped =", p1.pop())
for x in p1.list:
    print(x, end=" ")
print()

print("size = ", p1.size())