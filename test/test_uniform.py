import numpy as np
import pytest

from src.workloads.uniform import generate_uniform_workload


def test_uniform_workload_has_expected_shape_and_node_bounds():
    workload = generate_uniform_workload(
        num_nodes=8, num_requests=20, dim=2, seed=42
    )

    assert workload.shape == (20, 2)
    assert np.all((0 <= workload) & (workload < 8))


def test_uniform_workload_dim_one_is_flat():
    workload = generate_uniform_workload(
        num_nodes=8, num_requests=5, dim=1, seed=42
    )

    assert workload.shape == (5,)


def test_uniform_requests_contain_distinct_nodes():
    workload = generate_uniform_workload(
        num_nodes=8, num_requests=20, dim=4, seed=42
    )

    assert all(len(set(request)) == 4 for request in workload)


def test_uniform_workload_is_reproducible_with_seed():
    first = generate_uniform_workload(8, 10, 3, seed=42)
    second = generate_uniform_workload(8, 10, 3, seed=42)

    np.testing.assert_array_equal(first, second)


def test_uniform_workload_rejects_dimension_larger_than_node_count():
    with pytest.raises(ValueError, match="dim cannot exceed num_nodes"):
        generate_uniform_workload(num_nodes=2, num_requests=1, dim=3)
