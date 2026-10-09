class Node:
    """Represents a single node in the Binary Search Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree supporting insertion, search, deletion, and traversal."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts a new key into the BST."""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node  # Ignores duplicate keys

    def search(self, key) -> bool:
        """Returns True if the key exists in the tree, otherwise False."""
        return self._search(self.root, key)

    def _search(self, node, key) -> bool:
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        """Deletes a key from the BST if present."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1 & 2: Node has 0 or 1 child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 3: Node has 2 children
            # Find the in-order successor (smallest key in the right subtree)
            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return node

    def _min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self) -> list:
        """Returns keys in ascending order."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# Example Usage
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert elements
    for num in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(num)

    print("In-order traversal:", bst.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]

    # Search
    print("Search 40:", bst.search(40))  # True
    print("Search 90:", bst.search(90))  # False

    # Delete node with two children (50)
    bst.delete(50)
    print("After deleting 50:", bst.inorder_traversal())  # [20, 30, 40, 60, 70, 80]