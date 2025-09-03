class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

root = Node(50)
keys = [30, 20, 40, 70, 60, 80]

for key in keys:
    insert(root, key)

inorder(root)
print()
