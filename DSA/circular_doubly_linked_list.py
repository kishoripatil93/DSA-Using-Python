class Node:
    def __init__(self, prev = None, item = None, next = None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self, start = None):
        self.start = start

    def is_empty(self):
        return self.start == None
    
    def add_to_head(self, item):
        n = Node(None, item, self.start)
        if self.is_empty():
            n.prev = n
            n.next = n
            self.start = n
        else:
            last = self.start.prev

            n.next = self.start
            n.prev = last

            last.next = n
            self.start.prev = n
            self.start = n

    def add_to_tail(self, item):
        n = Node(None, item, None)
        if self.is_empty():
            n.prev = n
            n.next = n
            self.start = n
        else:
            last = self.start.prev
            n.next = self.start
            n.prev = self.start.prev
            last.next = n
            self.start.prev = n

    def search_elt_in_CDLL(self, item):
        if self.is_empty():
            return None
        
        first = self.start
        last = self.start.prev
        while first != last:
            if first.item == item:
                print(first.item, "Present in list")
                return first
            first = first.next
        if first.item == item:
            print(first.item, "Present in list")
            return first

        print(item, "Not present")
        return None

    def add_after(self, node, item):
        if node is not None:
            n = Node(None, item, None)
            n.prev = node
            n.next = node.next
            node.next.prev = n
            node.next = n

    def delete_first_node(self):
        if self.is_empty():
            return

        if self.start == self.start.prev:
            self.start = None
            return

        self.start.prev.next = self.start.next
        self.start.next.prev = self.start.prev
        self.start = self.start.next

    def delete_last_node(self):
        if self.is_empty():
            return
        
        if self.start == self.start.prev:
            self.start = None
            return  

        self.start.prev.prev.next =  self.start
        self.start.prev = self.start.prev.prev  

    def delete_item(self, item):
        if self.is_empty():
            return
        temp = self.start
        last = self.start.prev
        while True:
            if temp.item == item:

                if self.start == self.start.prev:
                    self.start = None
                    return
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev  
                
                if temp == self.start:
                    self.start = temp.next

                    return           

            if temp == last:
                break

            temp = temp.next

      

    def print_CDLL(self):
        if self.start is None:
            print()
            return
        
        temp = self.start
        last = self.start.prev
        while True:
            print(temp.item, end=" ")
            if temp == last:
                break

            temp = temp.next
        print()
        temp = self.start
        last = self.start.prev
        while True:
            print(last.item, end=" ")
            if temp == last:
                break

            last = last.prev
        print()

    def __iter__(self):
        return CDLLiter(self.start)

class CDLLiter:
    def __init__(self, start):
        self.start = start
        self.current = start
        self.first_pass = True

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration

        if not self.first_pass and self.current == self.start:
            raise StopIteration

        self.first_pass = False
        data = self.current.item
        self.current = self.current.next
        return data

myList = CDLL()
#Test add to head
def test_add_to_head():
    myList.add_to_head(10)
    myList.add_to_head(20)
    myList.add_to_head(30)
    myList.add_to_head(40)
    myList.print_CDLL()

# Test add to tail
def test_add_to_tail():
    myList.add_to_head(30)
    myList.add_to_tail(50)
    myList.add_to_head(40)
    myList.add_to_tail(60)
    myList.add_to_tail(70)
    myList.print_CDLL()
    for x in myList:
        print(x, end=" ")

    print()

# Test search function 
def test_search_elt_in_CDLL():
    test_add_to_tail()
    myList.search_elt_in_CDLL(70)
    myList.search_elt_in_CDLL(50)
    myList.search_elt_in_CDLL(40)
    myList.search_elt_in_CDLL(10)
    myList.search_elt_in_CDLL(30)

# Test insert after function
def test_add_after():
    myList.add_after(myList.search_elt_in_CDLL(30), 35)
    test_add_to_tail()
    myList.add_after(myList.search_elt_in_CDLL(30), 35)
    myList.print_CDLL()
    myList.add_after(myList.search_elt_in_CDLL(70), 75)
    myList.print_CDLL()

#test delete first node
def test_delete_first_node():
    myList.delete_first_node()
    myList.add_to_head(30)
    myList.print_CDLL()
    myList.delete_first_node()
    myList.print_CDLL()
    myList.add_to_head(20)
    myList.add_to_head(10)
    myList.print_CDLL()
    myList.delete_first_node()
    myList.print_CDLL()
    test_add_to_tail()
    myList.delete_first_node()
    myList.print_CDLL()

#test delete last node
def test_delete_last_node():
    myList.delete_last_node()
    myList.add_to_head(30)
    myList.print_CDLL()
    myList.delete_last_node()
    myList.print_CDLL()
    myList.add_to_head(20)
    myList.add_to_head(10)
    myList.print_CDLL()
    myList.delete_last_node()
    myList.print_CDLL()
    test_add_to_tail()
    myList.delete_last_node()
    myList.print_CDLL()
    myList.delete_last_node()
    myList.print_CDLL()

#test delete first node
def test_delete_item():
    myList.delete_item(30)
    myList.add_to_head(30)
    myList.print_CDLL()
    myList.delete_item(30)
    myList.print_CDLL()
    myList.add_to_head(20)
    myList.add_to_head(10)
    myList.print_CDLL()
    myList.delete_item(20)
    myList.print_CDLL()
    test_add_to_tail()
    test_add_to_tail()
    test_add_to_head()
    myList.delete_item(60)
    myList.print_CDLL()
    test_add_to_head()
    myList.delete_item(50)
    myList.print_CDLL()


test_add_to_head()
test_add_to_tail()
test_search_elt_in_CDLL()
test_add_after()
test_delete_first_node()
test_delete_last_node()
test_delete_item()

    
