from .bst import BinarySearchTree

def build_optimal_bst(num_nodes, requests):
    """Build an optimal binary search tree from the given request sequence.

    Args:
        num_nodes (int): The number of nodes in the tree.
        requests (list of int): The sequence of requests for the nodes.

    Returns:
        BinarySearchTree: The constructed optimal binary search tree.
    """
    tree = BinarySearchTree()

    frequencies = _frequencies_from_request_sequence(num_nodes, requests)
    dp_roots = _optimal_bst_roots(num_nodes, frequencies)
    insertion_order = _insertion_order_from_roots(dp_roots, 0, num_nodes - 1)
    for index in insertion_order:
        tree.insert(index)
    return tree

def _frequencies_from_request_sequence(num_nodes, requests):
    """Compute the frequencies of each node in the request sequence.

    Args:
        num_nodes (int): The number of nodes in the tree.
        requests (list of int): The sequence of requests for the nodes.

    Returns:
        list of int: The frequencies of each node in the request sequence.
    """
    frequencies = [0] * num_nodes
    for request in requests:
        if 0 <= request < num_nodes:
            frequencies[request] += 1
    return frequencies

def _optimal_bst_roots(num_nodes, frequencies):
    """Compute the root indices for an optimal binary search tree.

    Args:
        num_nodes (int): The number of nodes in the tree.
        frequencies (list of int): The frequencies of each node in the request sequence.

    Returns:
        list of list of int: The root indices for the optimal binary search tree.
    """

    prefix_sum = [0] * (num_nodes + 1)
    for i in range(num_nodes):
        prefix_sum[i + 1] = prefix_sum[i] + frequencies[i]

    dp_costs = [[0] * num_nodes for _ in range(num_nodes)]
    dp_roots = [[0] * num_nodes for _ in range(num_nodes)]

    for length in range(1, num_nodes + 1):
        for i in range(num_nodes - length + 1):
            j = i + length - 1
            dp_costs[i][j] = float('inf')
            for r in range(i, j + 1):
                left_cost = dp_costs[i][r - 1] if r > i else 0
                right_cost = dp_costs[r + 1][j] if r < j else 0
                total_cost = left_cost + right_cost + prefix_sum[j + 1] - prefix_sum[i]
                if total_cost < dp_costs[i][j]:
                    dp_costs[i][j] = total_cost
                    dp_roots[i][j] = r

    return dp_roots

def _insertion_order_from_roots(dp_roots, i, j):
    """Compute the insertion order for an optimal binary search tree from the root indices.

    Args:
        dp_roots (list of list of int): The root indices for the optimal binary search tree.
        i (int): The starting index of the current subtree.
        j (int): The ending index of the current subtree.

    Returns:
        list of int: The insertion order for the optimal binary search tree.
    """
    if i > j:
        return []
    r = dp_roots[i][j]
    return [r] + _insertion_order_from_roots(dp_roots, i, r - 1) + _insertion_order_from_roots(dp_roots, r + 1, j)
