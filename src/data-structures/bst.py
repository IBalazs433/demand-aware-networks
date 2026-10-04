from src.nodes.node import Node


class BinarySearchTree:
    """
    A class representing a binary search tree (BST).
    
    Attributes:
        root: The root node of the BST.
        search_cost: The cumulative cost of search operations, i.e., 
            the total number of nodes visited during all search operations.
    """

    def __init__(self):
        self.root = None
        self.search_cost = 0

    def insert(self, key):
        """
        Inserts a key into the BST and returns the inserted node.

        Args:
            key: The value to be inserted into the BST.

        Returns:
            The node that was inserted into the BST.
        """
        if not self.root:
            self.root = Node(key)
            return self.root
        else:
            return self._insert(self.root, key)

    def _insert(self, current_node, key):
        """
        Helper method to insert a key into the BST starting from the given node.

        Args:
            current_node: The node from which to start the insertion.
            key: The value to be inserted into the BST.

        Returns:
            The node that was inserted into the BST.
        """

        if key < current_node.key:
            if current_node.left:
                return self._insert(current_node.left, key)
            else:
                current_node.left = Node(key, parent=current_node)
                return current_node.left
        else:
            if current_node.right:
                return self._insert(current_node.right, key)
            else:
                current_node.right = Node(key, parent=current_node)
                return current_node.right

    def search(self, key):
        """
        Searches for a key in the BST and returns the node containing the key, if found.

        Args:
            key: The value to search for in the BST.

        Returns:
            The node containing the key if found, otherwise None.
        """
        current_node = self.root
        self.search_cost += 1

        while current_node and current_node.key != key:
            self.search_cost += 1
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node