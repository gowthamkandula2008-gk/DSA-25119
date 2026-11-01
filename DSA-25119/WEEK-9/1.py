class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None 
        self.right = None

# Insert a node
def insert(root, x): 
    if root is None: 
        return Node(x)
    if x < root.data:
        root.left = insert(root.left, x)
    elif x > root.data:
        root.right = insert(root.right, x)
    else:
        print("Duplicate value is not allowed.")
    return root

# Inorder Traversal: Left, Root, Right
def inorder(root): 
    if root is not None: 
        inorder(root.left) 
        print(root.data, end=" ") 
        inorder(root.right)

# Preorder Traversal: Root, Left, Right
def preorder(root): 
    if root is not None: 
        print(root.data, end=" ") 
        preorder(root.left) 
        preorder(root.right)

# Postorder Traversal: Left, Right, Root
def postorder(root): 
    if root is not None: 
        postorder(root.left) 
        postorder(root.right) 
        print(root.data, end=" ")

# Find minimum element
def find_min(root): 
    if root is None: 
        return None
    while root.left is not None:
        root = root.left
    return root

# Find maximum element
def find_max(root): 
    if root is None: 
        return None
    while root.right is not None:
        root = root.right
    return root

# Search for an element
def search(root, x): 
    if root is None: 
        return None
    if x < root.data:
        return search(root.left, x)
    elif x > root.data:
        return search(root.right, x)
    else:
        return root

# Count total nodes
def count_nodes(root): 
    if root is None: 
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Count leaf nodes
def count_leaves(root): 
    if root is None: 
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

# Count internal nodes
def count_internal(root): 
    if root is None: 
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + count_internal(root.left) + count_internal(root.right)

# Find height of the tree
def height(root): 
    if root is None: 
        return -1
    return 1 + max(height(root.left), height(root.right))

# Delete a node
def delete(root, x): 
    if root is None: 
        return None
    if x < root.data:
        root.left = delete(root.left, x)
    elif x > root.data:
        root.right = delete(root.right, x)
    else:
        # Case 1: No children
        if root.left is None and root.right is None:
            return None
        # Case 2: Only right child
        elif root.left is None:
            return root.right
        # Case 3: Only left child
        elif root.right is None:
            return root.left
        # Case 4: Two children
        successor = find_min(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root

# Level-order Traversal using a queue
def level_order(root): 
    if root is None: 
        return
    queue = [root]
    front = 0
    while front < len(queue):
        node = queue[front]
        front += 1
        print(node.data, end=" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

# Main menu-driven program
root = None
while True: 
    print("\n\n===== BINARY SEARCH TREE =====") 
    print("1. Insert")
    print("2. Preorder Traversal") 
    print("3. Inorder Traversal") 
    print("4. Postorder Traversal") 
    print("5. Find Minimum") 
    print("6. Find Maximum") 
    print("7. Search") 
    print("8. Delete") 
    print("9. Count Total Nodes") 
    print("10. Count Leaf Nodes") 
    print("11. Count Internal Nodes") 
    print("12. Find Height") 
    print("13. Level Order Traversal") 
    print("14. Exit")
    
    try:
        choice = int(input("Enter your choice: ")) 
    except ValueError:
        print("Please enter a valid integer choice.")
        continue

    if choice == 1:
        try:
            data = int(input("Enter the data to insert: "))
            existed = search(root, data) is not None
            root = insert(root, data)
            if not existed:
                print("Element inserted successfully.")
        except ValueError:
            print("Please enter an integer.")

    elif choice == 2:
        print("Preorder Traversal:", end=" ")
        if root is None:
            print("Tree is empty.")
        else:
            preorder(root)
            print()

    elif choice == 3:
        print("Inorder Traversal:", end=" ")
        if root is None:
            print("Tree is empty.")
        else:
            inorder(root)
            print()

    elif choice == 4:
        print("Postorder Traversal:", end=" ")
        if root is None:
            print("Tree is empty.")
        else:
            postorder(root)
            print()

    elif choice == 5:
        node = find_min(root)
        if node is None:
            print("Tree is empty.")
        else:
            print("Minimum element:", node.data)

    elif choice == 6:
        node = find_max(root)
        if node is None:
            print("Tree is empty.")
        else:
            print("Maximum element:", node.data)

    elif choice == 7:
        try:
            data = int(input("Enter the element to search: "))
            if search(root, data) is not None:
                print("Element", data, "is found.")
            else:
                print("Element", data, "is not found.")
        except ValueError:
            print("Please enter an integer.")

    elif choice == 8:
        try:
            data = int(input("Enter the element to delete: "))
            if search(root, data) is None:
                print("Element not found.")
            else:
                root = delete(root, data)
                print("Element deleted successfully.")
        except ValueError:
            print("Please enter an integer.")

    elif choice == 9:
        print("Number of nodes:", count_nodes(root))

    elif choice == 10:
        print("Number of leaf nodes:", count_leaves(root))

    elif choice == 11:
        print("Number of internal nodes:", count_internal(root))

    elif choice == 12:
        print("Height of BST:", height(root))

    elif choice == 13:
        print("Level Order Traversal:", end=" ")
        if root is None:
            print("Tree is empty.")
        else:
            level_order(root)
            print()

    elif choice == 14:
        print("Program terminated.")
        break

    else:    
        print("Invalid choice. Please try again.")
