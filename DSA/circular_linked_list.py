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

        n.next = self.last.next
        self.last.next = n
        return
    
    def add_to_tail(self, item):
        n = Node(item)
        if self.last is None:
            self.last = n
            n.next = n
            return

        n.next = self.last.next
        self.last.next = n
        self.last = n
        return
    
    def search_item_in_cll(self, item):
        if self.last is None:
            return None
        
        temp = self.last.next
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
        if node is not None:
            n = Node(item, node.next)
            node.next = n
            if node == self.last:
                self.last = n
 
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
myList.delete_last_node()
myList.print_CLL()
myList.delete_first_node()
myList.print_CLL
myList.delete_last_node()
myList.print_CLL()
myList.add_to_head(10)
myList.print_CLL()
myList.delete_last_node()
myList.print_CLL()
myList.add_to_head(20)
myList.print_CLL()
myList.delete_last_node()
myList.print_CLL()
myList.add_to_head(30)
myList.print_CLL()
myList.add_to_head(40)
myList.print_CLL()
myList.delete_last_node()
myList.print_CLL()
myList.add_to_tail(50)
myList.print_CLL()
myList.add_to_tail(60)
myList.print_CLL()
myList.delete_last_node()
myList.print_CLL()
myList.delete_first_node()
myList.print_CLL()
myList.search_item_in_cll(10)
myList.search_item_in_cll(60)
myList.insert_after(myList.search_item_in_cll(10), 50)
myList.print_CLL()
myList.delete_last_node()
myList.print_CLL()
myList.print_CLL()
myList.delete_first_node()
myList.print_CLL()
myList.add_to_head(40)
myList.add_to_tail(50)
myList.print_CLL()
myList.add_to_tail(60)
myList.print_CLL()
myList.insert_after(myList.search_item_in_cll(60), 65)
myList.print_CLL()
myList.add_to_head(35)
myList.print_CLL()
myList.search_item_in_cll(60)
myList.add_to_tail(70)
myList.print_CLL()
myList.insert_after(myList.search_item_in_cll(70), 75)
myList.print_CLL()
myList.delete_first_node()
myList.print_CLL()

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

