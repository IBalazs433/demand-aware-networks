import random

from src.data_structures.bst import BinarySearchTree
from src.data_structures.optimal_bst import build_optimal_bst_from_roots


def _search_sequence_cost(tree, requests):
    for request in requests:
        tree.search(request)
    return tree.search_cost


def test_optimal_bst_has_no_greater_search_cost_than_random_bsts():
    num_nodes = 8
    requests = (
        [3] * 40
        + [6] * 20
        + [1] * 10
        + [0, 2, 4, 5, 7] * 2
    )

    optimal_tree = build_optimal_bst_from_roots(num_nodes, requests)
    optimal_cost = _search_sequence_cost(optimal_tree, requests)

    random_costs = []
    for seed in range(50):
        insertion_order = random.Random(seed).sample(range(num_nodes), num_nodes)
        random_tree = BinarySearchTree()
        for key in insertion_order:
            random_tree.insert(key)
        random_costs.append(_search_sequence_cost(random_tree, requests))

    assert optimal_cost <= min(random_costs)
    assert all(optimal_cost <= cost for cost in random_costs)


def test_optimal_bst_contains_each_key_and_preserves_bst_order():
    num_nodes = 6
    requests = [2] * 12 + [4] * 6 + [0, 1, 3, 5]

    tree = build_optimal_bst_from_roots(num_nodes, requests)

    assert [tree.search(key).key for key in range(num_nodes)] == list(range(num_nodes))
