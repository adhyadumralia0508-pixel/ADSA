class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

root = None

n = int(input("Enter number of elements: "))

print("Enter elements:")

for i in range(n):
    data = int(input())
    root = insert(root, data)


print("\nPreorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)


key = int(input("\n\nEnter key to search: "))

if search(root, key):
    print("Key found")
else:
    print("Key not found")