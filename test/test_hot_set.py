import numpy as np
import pytest

from src.workloads.hot_set import generate_hot_set_workload


def test_hot_set_workload_has_expected_shape_and_node_bounds():
    workload = generate_hot_set_workload(
        num_nodes=10,
        num_requests=20,
        dim=2,
        hot_set_frac=0.4,
        hot_set_prob=0.8,
        seed=42,
    )

    assert workload.shape == (20, 2)
    assert np.all((0 <= workload) & (workload < 10))


def test_hot_set_workload_dim_one_is_flat():
    workload = generate_hot_set_workload(
        num_nodes=10,
        num_requests=5,
        dim=1,
        hot_set_frac=0.4,
        hot_set_prob=0.8,
        seed=42,
    )

    assert workload.shape == (5,)


def test_hot_set_requests_contain_distinct_nodes():
    workload = generate_hot_set_workload(
        num_nodes=10,
        num_requests=20,
        dim=4,
        hot_set_frac=0.5,
        hot_set_prob=1.0,
        seed=42,
    )

    assert all(len(set(request)) == 4 for request in workload)


def test_hot_set_workload_falls_back_when_hot_set_is_empty():
    workload = generate_hot_set_workload(
        num_nodes=5,
        num_requests=5,
        dim=2,
        hot_set_frac=0,
        hot_set_prob=1.0,
        seed=42,
    )

    assert np.all((0 <= workload) & (workload < 5))
    assert all(len(set(request)) == 2 for request in workload)


def test_hot_set_workload_is_reproducible_with_seed():
    args = (10, 10, 3, 0.5, 0.8)

    first = generate_hot_set_workload(*args, seed=42)
    second = generate_hot_set_workload(*args, seed=42)

    np.testing.assert_array_equal(first, second)


def test_hot_set_workload_rejects_dimension_larger_than_node_count():
    with pytest.raises(ValueError, match="dim cannot exceed num_nodes"):
        generate_hot_set_workload(2, 1, 3, 0.5, 0.5)
