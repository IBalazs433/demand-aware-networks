from src.nodes.node import Node


class BinarySearchTreeNetwork:
    """
    A class representing a binary search tree network.

    Attributes:
        root (Node): The root node of the binary search tree.
        communication_cost (int): The total communication cost incurred by requests, i.e.,
            the sum of the path lengths for all requests made in the network.
    """
    def __init__(self):
        self.root = None
        self.communication_cost = 0

    def insert(self, key):
        """
        Inserts a new node with the given key into the binary search tree.

        Args:
            key: The key of the node to be inserted.

        Returns:
            Node: The newly inserted node.
        """
        if self.root is None:
            self.root = Node(key)
            return self.root
        else:
            return self._insert(self.root, key)

    def _insert(self, current_node, key):
        """
        Helper method to insert a new node with the given key into the binary search tree.

        Args:
            current_node (Node): The current node being examined.
            key: The key of the node to be inserted.

        Returns:
            Node: The newly inserted node.
        """
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
                return current_node.left
            else:
                return self._insert(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
                return current_node.right
            else:
                return self._insert(current_node.right, key)

    def search(self, key):
        """
        Searches for a node with the given key in the binary search tree.

        Args:
            key: The key of the node to search for.

        Returns:
            tuple: A tuple containing the found node (or None if not found) and its depth in the tree.
        """
        current_node = self.root
        depth = 0

        while current_node and current_node.key != key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
            depth += 1

        if current_node is None:
            return None, depth
        return current_node, depth

    def request(self, sender_key, receiver_key):
        """
        Handles a request from a sender node to a receiver node in the binary search tree network.

        Args:
            sender_key: The key of the sender node.
            receiver_key: The key of the receiver node.

        Returns:
            int: The path length between the sender and receiver nodes, or None if any of the nodes are not found.
        """
        lca_node, lca_depth = self._lca(sender_key, receiver_key)
        sender_node, sender_depth = self.search(sender_key)
        receiver_node, receiver_depth = self.search(receiver_key)

        if lca_node is None or sender_node is None or receiver_node is None:
            return None

        path_length = sender_depth + receiver_depth - 2 * lca_depth
        self.communication_cost += path_length
        return path_length

    def _lca(self, key1, key2):
        """
        Finds the lowest common ancestor (LCA) of two nodes with the given keys in the binary search tree.

        Args:
            key1: The key of the first node.
            key2: The key of the second node.

        Returns:
            tuple: A tuple containing the LCA node (or None if not found) and its depth in the tree.
        """
        current_node = self.root
        depth = 0

        while current_node:
            if key1 < current_node.key and key2 < current_node.key:
                current_node = current_node.left
                depth += 1
            elif key1 > current_node.key and key2 > current_node.key:
                current_node = current_node.right
                depth += 1
            else:
                return current_node, depth
        return None, depth

    