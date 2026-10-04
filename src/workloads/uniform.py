import numpy as np


def generate_uniform_workload(num_nodes, num_requests, dim, seed=None):
    """
    Generates a uniform workload for a network.
    Nodes are not repeated within an individual request.

    Args:
        num_nodes: The number of nodes in the network.
        num_requests: The number of requests to generate.
        dim: Number of coordinates in each request.
        seed: An optional random seed for reproducibility.

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
        workload[i] = np.random.choice(num_nodes, size=dim, replace=False)

    return workload[:, 0] if dim == 1 else workload