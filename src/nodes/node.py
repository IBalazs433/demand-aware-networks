class Node:
    """
    A class representing a node in a binary tree.

    Attributes:
        key: The value stored in the node.
        parent: The parent node of this node.
        left: The left child node.
        right: The right child node.

    Properties:
        is_left_child: Returns True if this node is the left child of its parent.
        is_right_child: Returns True if this node is the right child of its parent.
    """

    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        """
        Returns a string representation of the node.
        """
        return f"Node(key={self.key})"

    @property
    def is_left_child(self):
        """
        Returns True if this node is the left child of its parent.
        """
        return self.parent and self.parent.left == self

    @property
    def is_right_child(self):
        """
        Returns True if this node is the right child of its parent.
        """
        return self.parent and self.parent.right == self