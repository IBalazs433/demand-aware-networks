from .bst_network import BinarySearchTreeNetwork

def build_optimal_bst_network(num_nodes, requests):
    """Build an optimal binary search tree network from the given request sequence.

    Args:
        num_nodes (int): The number of nodes in the network.
        requests (list of int): The sequence of requests for the nodes.

    Returns:
        BinarySearchTreeNetwork: The constructed optimal binary search tree network.
    """
    network = BinarySearchTreeNetwork()

    request_matrix = _build_request_matrix(num_nodes, requests)
    dp_roots = _optimal_bst_network_roots(num_nodes, request_matrix)
    insertion_order = _insertion_order_from_roots(dp_roots, 0, num_nodes - 1)
    for index in insertion_order:
        network.insert(index)
    return network

def _build_request_matrix(num_nodes, requests):
    """Build the request matrix for the optimal BST network.

    Args:
        num_nodes (int): The number of nodes in the network.
        requests (list of tuple of int): The sequence of requests for the nodes.

    Returns:
        list of list of int: The request matrix for the optimal BST network.
    """
    request_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    for request in requests:
        if 0 <= request[0] < num_nodes and 0 <= request[1] < num_nodes:
            request_matrix[request[0]][request[1]] += 1
    return request_matrix

def _optimal_bst_network_roots(num_nodes, request_matrix):
    """Compute the root indices for an optimal binary search tree network.

    Args:
        num_nodes (int): The number of nodes in the network.
        request_matrix (list of list of int): The request matrix for the optimal BST network.

    Returns:
        list of list of int: The root indices for the optimal binary search tree network.
    """
    dp_cost = [[0] * num_nodes for _ in range(num_nodes)]
    dp_roots = [[0] * num_nodes for _ in range(num_nodes)]

    # Precompute interval weights
    W = [[None for _ in range(num_nodes)] for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i, num_nodes):
            vec = [0 for _ in range(num_nodes)]
            for v in range(i, j + 1):
                total = 0
                for u in range(num_nodes):
                    if not (i <= u <= j):
                        total += request_matrix[u][v] + request_matrix[v][u]
                vec[v] = total
            W[i][j] = vec

    # Base case: single node intervals
    for i in range(num_nodes):
        dp_cost[i][i] = 0
        dp_roots[i][i] = i

    # Fill DP table for larger intervals
    for length in range(2, num_nodes + 1):
        for i in range(0, num_nodes - length + 1):
            j = i + length - 1
            best_cost = float('inf')
            best_root = -1

            WI = W[i][j]
            for root in range(i, j + 1):
                cost = 0
                if root > i:
                    cost += dp_cost[i][root - 1]
                if root < j:
                    cost += dp_cost[root + 1][j]

                for v in range(i, root):
                    cost += WI[v]
                for v in range(root + 1, j + 1):
                    cost += WI[v]
                if cost < best_cost:
                    best_cost = cost
                    best_root = root

            dp_cost[i][j] = best_cost
            dp_roots[i][j] = best_root

    return dp_roots

def _insertion_order_from_roots(dp_roots, i, j):
    """Compute the insertion order for an optimal binary search tree network from the root indices.

    Args:
        dp_roots (list of list of int): The root indices for the optimal binary search tree network.
        i (int): The starting index of the current subtree.
        j (int): The ending index of the current subtree.

    Returns:
        list of int: The insertion order for the optimal binary search tree network.
    """
    if i > j:
        return []
    r = dp_roots[i][j]
    return [r] + _insertion_order_from_roots(dp_roots, i, r - 1) + _insertion_order_from_roots(dp_roots, r + 1, j)
