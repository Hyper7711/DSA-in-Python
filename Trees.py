"""BINARY TREE REPRESENTATION"""

class Node:
    """Represents a single node in a binary tree."""

    def __init__(self, data):
        self.data = data    #initialize NODE
        self.left = None    #SET LEFT NODE
        self.right = None   #SET RIGHT NODE

class BinaryTree:

    def __init__(self, root_data):
        """Initialize a tree with the root node."""
        self.root = Node(root_data)


    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node)
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")

if __name__ == "__main__":
    # Creating a sample binary tree
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Inorder Traversal:")
    tree.inorder_traversal(tree.root)

    print("\nPreorder Traversal:")
    tree.preorder_traversal(tree.root)

    print("\nPostorder Traversal:")
    tree.postorder_traversal(tree.root)

