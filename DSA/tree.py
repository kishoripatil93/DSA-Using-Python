class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self, root = None):
        self.root = root

    def is_empty(self):
        return self.root == None
    
    def r_insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            print("root= ",root.item)
            root.left = self.r_insert(root.left, data)
        elif data > root.item:
            root.right = self.r_insert(root.right, data)   
        return root

    def insert(self, data):
        self.root = self.r_insert(self.root, data)

    def r_search(self, node, data):
        if node is None or node.item == data:
            return node
        if data < node.item:
            return self.r_search(node.left, data)
        else:
            return self.r_search(node.right, data)


    def search(self, data):
        return self.r_search(self.root, data)

    # Preorder DFS - Left, Root, Right
    def r_preorder(self, root, result):
        if root is not None:
            result.append(root.item)
            self.r_preorder(root.left, result)
            self.r_preorder(root.right, result)

    # DFS - Root, Left, Right
    def preorder(self):
        result = []
        self.r_preorder(self.root, result)
        return result

    # Inorder DFS - Left, Root, Right
    def r_inorder(self, root, result):
        if root == None:
            return None
        else:
            self.r_inorder(root.left, result)
            result.append(root.item)
            self.r_inorder(root.right, result)

    # DFS - Left, Root, Right
    def inorder(self):
        result = []
        self.r_inorder(self.root, result)
        return result
    
    # Postorder DFS - Left, Right, Root
    def r_postorder(self, root, result):
        if root is not None:
            self.r_postorder(root.left, result)
            self.r_postorder(root.right, result)
            result.append(root.item)

    def postorder(self):
        result = []
        self.r_postorder(self.root, result)
        return result




b1 = BST()
b1.insert(50)
b1.insert(30)
b1.insert(60)
b1.insert(35)
b1.insert(65)
b1.insert(55)
n = b1.search(60)
if n is not None:
    print("found elt", n.item)

print("Tree nodes in inorder are as following")
nodes = b1.inorder()
for i in nodes:
    print(i, end=" ")
print()

print("Tree nodes in preorder are as following")
nodes = b1.preorder()
for i in nodes:
    print(i, end=" ")
print()

print("Tree nodes in postorder are as following")
nodes = b1.postorder()
for i in nodes:
    print(i, end=" ")
print()




            

            

