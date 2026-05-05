class Deque:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def insertion_first(self, data):
        self.list.insert(0, data)

    def insertion_last(self, data):
        self.list.append(data)

    def remove_first(self):
        if self.is_empty():
            return

        self.list.pop(0)


    def remove_last(self):
        if self.is_empty():
            return
        self.list.pop(-1)

    def ret_item_count(self):
        return len(self.list)
    
    def get_front(self):
        if self.is_empty():
            return
        return self.list[0]
    
    def get_rear(self):
        if self.is_empty():
            return
        return self.list[-1]

d1 = Deque()
d1.insertion_first(10)
d1.insertion_first(20)
d1.insertion_last(30)
for x in d1.list:
    print(x, end=" ")
print()
print("item count is ", d1.ret_item_count())
print("front ", d1.get_front(), "rear ", d1.get_rear())
print("\n")

d1.remove_last()
for x in d1.list:
    print(x, end=" ")
print()
print("item count is ", d1.ret_item_count())
print("front ", d1.get_front(), "rear ", d1.get_rear())
print("\n")

d1.remove_first()
for x in d1.list:
    print(x, end=" ")
print()
print("item count is ", d1.ret_item_count())
print("front ", d1.get_front(), "rear ", d1.get_rear())
print("\n")

d1.remove_first()
for x in d1.list:
    print(x, end=" ")
print()
print("item count is ", d1.ret_item_count())
print("front ", d1.get_front(), "rear ", d1.get_rear())
print("\n")