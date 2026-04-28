
'''''
class CLL:
    def __init__(self, head = None):
        self.head = head

    def is_empty(self):
        return self.head == None

    def add_to_head(self, item):
        n = Node(item, self.head)
        if self.head is None:
            n.next = n
            self.head = n
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next

            temp.next = n
            self.head = n

    def add_to_tail(self, item):
        n = Node(item, self.head)
        if self.head is None:
            n.next = n
            self.head = n
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next

            temp.next = n

    def search_item_in_CLL(self, item):
        if self.is_empty():
            return
        
        temp = self.head
        while temp is not None:
            if item == temp.item:
                print(temp.item, " is Found in CLL")
                return temp
            temp = temp.next
             
            if temp == self.head:
                break

        print(item, " is not in CLL")
        return None


    def add_in_between(self, node, item):
        if self.is_empty():
            return
 
        temp = self.head
        while True:
            if temp.item == node:
                n = Node(item, temp.next)
                temp.next = n

            temp = temp.next

            if temp == self.head:
                break

    def print_CLL(self):
        if self.is_empty():
            print()
            return
        
        temp = self.head
        while True:
            print(temp.item, end=" ")
            temp = temp.next
            if temp == self.head:
                break

        print()

    def delete_first_node(self):
        if self.is_empty():
            return
        if self.head.next == self.head:
            self.head = None
            return
    
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next                

    def delete_last_elt(self):
        if self.is_empty():
            return
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head'''

'''''
    def add_to_tail(self, item):
        n = Node(item, self.last)
        if self.is_empty():
            self.last = n
            n.next = self.last
        else:
            self.last.next = n
            n.next = self.last'''


class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last = None):
        self.last = last

    def is_empty(self):
       return self.last == None
    
    def add_to_head(self, item):
        n = Node(item)
        if self.last is None:
            self.last = n
            n.next = n
            return
        head = self.last.next
        n.next = head
        self.last.next = n
        return
    
    def add_to_tail(self, item):
        n = Node(item)
        if self.last is None:
            self.last = n
            n.next = n
            return
        head = self.last.next
        self.last.next = n
        n.next = head
        self.last = n
        return
    
    def search_item_in_cll(self, item):
        if self.last is None:
            return None
        
        temp = self.last.next
        print(temp.item)
        while True:
            if temp.item == item:
                print(temp.item, "is found in cll")
                return temp
            
            if temp is self.last:
                break

            temp = temp.next

        print(item, "not found in cll")
        return None

    def insert_after(self, node, item):
        if self.last is None:
            raise ValueError("List is Empty")
        temp = self.last.next
        while True:
            if temp is node:
                n = Node(item)
                n.next = temp.next
                temp.next = n

                if self.last is temp:
                    self.last = n

                return
            
            if temp is self.last:
                break

            temp = temp.next

    def delete_first_node(self):
        if self.is_empty():
            return
        if self.last is self.last.next:
            self.last = None
            return
        self.last.next = self.last.next.next

    def delete_last_node(self):
        if self.is_empty():
            return
        if self.last == self.last.next:
            self.last = None
            return
        temp = self.last.next
        while temp.next is not self.last:
            temp = temp.next

        temp.next = self.last.next
        self.last = temp


    def delete_node(self, item):
        if self.is_empty():
            return
        
        temp = self.last

        while True:
            if temp.next.item == item:
                # only one node
                if temp == temp.next:
                    self.last = None

                # deleting last node
                elif temp.next == self.last:
                    temp.next = self.last.next
                    self.last = temp

                # deleting head or middle
                else:
                    temp.next = temp.next.next

                return

            temp = temp.next
            if temp == self.last:
                break

    def print_CLL(self):
        if self.is_empty():
            print()
            return
        temp = self.last.next
        while True:
            print(temp.item, end=" ")
            if temp is self.last:
                break
            temp = temp.next
        print()

    def __iter__(self):
        return CLLIerator(self.last.next)

class CLLIerator:
    def __init__(self, last):
        self.last = last
        self.firstNode = None

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.firstNode is not None and self.last == self.firstNode:
            raise StopIteration
        if self.firstNode is None:
            self.firstNode = self.last
        data = self.last.item
        self.last = self.last.next
        return data

# Testing circular linked list
myList = CLL()
# myList.delete_last_node()
# myList.print_CLL()
# myList.delete_first_node()
# myList.print_CLL
# myList.delete_last_node()
# myList.print_CLL()
# myList.add_to_head(10)
# myList.print_CLL()
# myList.delete_last_node()
# myList.print_CLL()
# myList.add_to_head(20)
# myList.print_CLL()
# myList.delete_last_node()
# myList.print_CLL()
# myList.add_to_head(30)
# myList.print_CLL()
# myList.add_to_head(40)
# myList.print_CLL()
# myList.delete_last_node()
# myList.print_CLL()
# myList.add_to_tail(50)
# myList.print_CLL()
# myList.add_to_tail(60)
# myList.print_CLL()
# myList.delete_last_node()
# myList.print_CLL()
# myList.delete_first_node()
# myList.print_CLL()
# myList.search_item_in_cll(10)
# myList.search_item_in_cll(60)
# myList.insert_after(myList.search_item_in_cll(10), 50)
# myList.print_CLL()
# # myList.delete_last_node()
# # myList.print_CLL()
# myList.print_CLL()
# myList.delete_first_node()
# myList.print_CLL()
# myList.add_to_head(40)
# myList.add_to_tail(50)
# myList.print_CLL()
# myList.add_to_tail(60)
# myList.print_CLL()
# myList.add_in_between(20, 45)
# myList.print_CLL()
# myList.add_to_head(35)
# myList.print_CLL()
# myList.add_in_between(35, 65)
# myList.print_CLL()
# # myList.search_item_in_CLL(60)
# myList.add_to_tail(60)
# # myList.print_CLL()
# # myList.delete_first_node()
# # myList.print_CLL()
# # myList.delete_last_elt()
# myList.print_CLL()

#########Delete node testing##########
myList.delete_node(12)
myList.print_CLL()
myList.add_to_head(10)
myList.print_CLL()
myList.delete_node(10)
myList.print_CLL()
myList.add_to_head(10)
myList.print_CLL()
myList.add_to_head(20)
myList.print_CLL()
myList.add_to_head(30)
myList.print_CLL()
myList.add_to_head(40)
myList.print_CLL()
myList.add_to_tail(50)
myList.print_CLL()
myList.delete_node(50)
myList.print_CLL()
for x in myList:
    print(x, end=" ")
print()

