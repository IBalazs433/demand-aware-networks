from src.nodes.node import Node


def test_node_initializes_key_parent_and_children():
    parent = Node(10)
    node = Node(5, parent=parent)

    assert node.key == 5
    assert node.parent is parent
    assert node.left is None
    assert node.right is None


def test_node_child_properties():
    parent = Node(10)
    left = Node(5, parent=parent)
    right = Node(15, parent=parent)
    parent.left = left
    parent.right = right

    assert left.is_left_child
    assert not left.is_right_child
    assert right.is_right_child
    assert not right.is_left_child


def test_node_string_representation():
    assert str(Node(7)) == "Node(key=7)"
