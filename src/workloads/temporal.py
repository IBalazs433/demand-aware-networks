import numpy as np


def generate_temporal_workload(num_nodes, num_requests, dim, repeat_prob, seed=None):
    """
    Generates a temporal workload for a network.
    Nodes are not repeated within an individual request.

    Args:
        num_nodes: The number of nodes in the network.
        num_requests: The number of requests to generate.
        dim: Number of coordinates in each request.
        repeat_prob: The probability of repeating the previous request.

    Returns:
        np.ndarray: Shape (num_requests,) when dim is 1, otherwise
            (num_requests, dim).
    """
    if seed is not None:
        np.random.seed(seed)

    if dim > num_nodes:
        raise ValueError("dim cannot exceed num_nodes when requests must have unique nodes.")

    workload = np.empty((num_requests, dim), dtype=int)
    for i in range(num_requests):
        if i > 0 and np.random.rand() < repeat_prob:
            workload[i] = workload[i - 1]
        else:
            workload[i] = np.random.choice(num_nodes, size=dim, replace=False)

    return workload[:, 0] if dim == 1 else workload