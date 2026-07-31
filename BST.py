class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert():
    x = int(input("Enter value (-1 for no node): "))
    if x == -1:
        return None

    root = Node(x)
    root.left = insert()
    root.right = insert()
    return root

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

root = insert()

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

Ouput:Preorder: 1 2 3
      Inorder: 3 2 1
      Postorder: 3 2 1