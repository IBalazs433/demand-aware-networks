from src.data_structures.bst import BinarySearchTree


def test_insert_builds_tree_and_sets_parent_links():
    tree = BinarySearchTree()

    root = tree.insert(10)
    left = tree.insert(5)
    right = tree.insert(15)

    assert tree.root is root
    assert root.left is left
    assert root.right is right
    assert left.parent is root
    assert right.parent is root


def test_duplicate_keys_are_inserted_to_the_right():
    tree = BinarySearchTree()

    first = tree.insert(10)
    second = tree.insert(10)

    assert first.right is second
    assert second.parent is first


def test_search_returns_node_and_counts_visited_nodes():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)

    assert tree.search(5) is tree.root.left
    assert tree.search_cost == 2


def test_search_returns_none_for_missing_key_and_counts_visits():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(5)

    assert tree.search(3) is None
    assert tree.search_cost == 3


def test_search_empty_tree_returns_none_and_counts_one_visit():
    tree = BinarySearchTree()

    assert tree.search(1) is None
    assert tree.search_cost == 1
