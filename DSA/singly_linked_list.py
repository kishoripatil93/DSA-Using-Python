#Signgly linked list

class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if(True != self.is_empty()):
            temp = self.start
            while None != temp.next:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search_elt_in_list(self, elt):
        temp = self.start
        while None != temp:
            if elt == temp.item:
                return temp
            temp = temp.next

        print("Element not present in list")
        return None
    
    def insert_in_between_node(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def print_list_elt(self):
        temp = self.start
        while None != temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def del_first_elt_in_list(self):
        if self.start is not None:
            self.start = self.start.next

    def del_last_elt_in_list(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

    def delete_item(self, item):
        if self.start is None:
            return
        
        if self.start.item == item:
            self.start = self.start.next
            return
        
        temp = self.start
        while temp is not None:   
            if temp.item != item:
                pass
            else:
                temp1.next = temp.next
            temp1 = temp
            temp = temp.next


    def delete_item_omkar(self, item):
        # Check for the head to be None
        if self.start is None:
            return
        
        if self.start.item == item:
            self.start = self.start.next
            return
        
        head = self.start
        prevNode = None
        while head is not None:
            if head.item == item:
                prevNode.next = head.next
                return
            prevNode = head
            head = head.next

    def __iter__(self):
        return SLLIterator(self.start)

class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
    

myList = SLL()
myList.delete_item(50)
myList.del_last_elt_in_list()
myList.del_first_elt_in_list()
myList.insert_at_start(40)
myList.del_last_elt_in_list()
myList.insert_at_start(60)
myList.insert_at_start(50)
myList.print_list_elt()
print("Deleting 50")
myList.delete_item(50)
print("Done")
myList.print_list_elt()
myList.del_last_elt_in_list()
myList.print_list_elt()
myList.search_elt_in_list(50)
myList.insert_at_start(50)
myList.insert_at_start(10)
myList.insert_in_between_node(myList.search_elt_in_list(50), 40)
myList.print_list_elt()
myList.insert_at_last(60)
myList.print_list_elt()
myList.insert_in_between_node(myList.search_elt_in_list(30), 35)
myList.print_list_elt()
myList.insert_in_between_node(myList.search_elt_in_list(40), 45)
myList.print_list_elt()
myList.delete_item(30)
myList.print_list_elt()
myList.del_last_elt_in_list()
myList.print_list_elt()
myList.delete_item(50)
myList.print_list_elt()
myList.delete_item(10)
myList.print_list_elt()
myList.delete_item(45)
myList.print_list_elt()
for x in myList:
    print(x, end=" ")

print()


    
    