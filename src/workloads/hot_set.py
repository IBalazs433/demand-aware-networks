import numpy as np


def generate_hot_set_workload(num_nodes, num_requests, dim, hot_set_frac, hot_set_prob, seed=None):
    """
    Generates a hot set workload for a network.
    Nodes are not repeated within an individual request.

    Args:
        num_nodes: The number of nodes in the network.
        num_requests: The number of requests to generate.
        dim: Number of coordinates in each request.
        hot_set_frac: The fraction of nodes that belong to the hot set (number of frequently accessed nodes).
        hot_set_prob: The probability of selecting a node from the hot set.

    Returns:
        np.ndarray: Shape (num_requests,) when dim is 1, otherwise
            (num_requests, dim).
    """
    if seed is not None:
        np.random.seed(seed)

    if dim > num_nodes:
        raise ValueError("dim cannot exceed num_nodes when requests must have unique nodes.")

    hot_set_size = int(num_nodes * hot_set_frac)
    hot_set = np.random.choice(num_nodes, size=hot_set_size, replace=False)
    workload = np.empty((num_requests, dim), dtype=int)
    nodes = np.arange(num_nodes)
    for i in range(num_requests):
        request = np.empty(dim, dtype=int)
        for j in range(dim):
            available_nodes = nodes[~np.isin(nodes, request[:j])]
            available_hot_nodes = hot_set[np.isin(hot_set, available_nodes)]
            if np.random.rand() < hot_set_prob and available_hot_nodes.size:
                request[j] = np.random.choice(available_hot_nodes)
            else:
                request[j] = np.random.choice(available_nodes)
        workload[i] = request

    return workload[:, 0] if dim == 1 else workload