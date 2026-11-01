# Binary Tree Using Linked List
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None

class BinaryTree: 
    def __init__(self): 
        self.root = None

    # Insert root
    def set_root(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            print("Root already exists!")

    # Set left child
    def set_left(self, parent, data):
        node = self.search(parent)

        if node is None:
            print("Parent node not found!")
        elif node.left is not None:
            print("Left child already exists!")
        else:
            node.left = Node(data)

    # Set right child
    def set_right(self, parent, data):
        node = self.search(parent)

        if node is None:
            print("Parent node not found!")
        elif node.right is not None:
            print("Right child already exists!")
        else:
            node.right = Node(data)

    # Search for a node by its value
    def search(self, data):
        if self.root is None:
            return None

        queue = [self.root]

        while queue:
            node = queue.pop(0)

            if node.data == data:
                return node

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return None

    # Preorder: Root, Left, Right
    def preorder(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Inorder: Left, Root, Right
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Postorder: Left, Right, Root
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    # Level-order traversal
    def level_order(self):
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    # Display tree using preorder
    def display(self):
        if self.root is None:
            print("Tree is empty!")
        else:
            self.preorder(self.root)
            print()
 
# Main Program
tree = BinaryTree()
tree.set_root('A')
tree.set_left('A', 'B') 
tree.set_right('A', 'C')
tree.set_left('B', 'D') 
tree.set_right('B', 'E')
tree.set_right('C', 'F')

print("Binary Tree (Preorder): ", end="") 
tree.display()

print("Preorder Traversal: ", end="") 
tree.preorder(tree.root)

print("\nInorder Traversal: ", end="") 
tree.inorder(tree.root)

print("\nPostorder Traversal: ", end="") 
tree.postorder(tree.root)

print("\nLevel-order Traversal: ", end="") 
tree.level_order()
print()
