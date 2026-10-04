import numpy as np
import pytest

from src.workloads.temporal import generate_temporal_workload


def test_temporal_workload_has_expected_shape_and_node_bounds():
    workload = generate_temporal_workload(
        num_nodes=8,
        num_requests=20,
        dim=2,
        repeat_prob=0.5,
        seed=42,
    )

    assert workload.shape == (20, 2)
    assert np.all((0 <= workload) & (workload < 8))


def test_temporal_workload_dim_one_is_flat():
    workload = generate_temporal_workload(
        num_nodes=8, num_requests=5, dim=1, repeat_prob=0.5, seed=42
    )

    assert workload.shape == (5,)


def test_temporal_requests_contain_distinct_nodes():
    workload = generate_temporal_workload(
        num_nodes=8, num_requests=20, dim=4, repeat_prob=0.5, seed=42
    )

    assert all(len(set(request)) == 4 for request in workload)


def test_temporal_workload_repeats_previous_request_when_probability_is_one():
    workload = generate_temporal_workload(
        num_nodes=8, num_requests=10, dim=3, repeat_prob=1.0, seed=42
    )

    assert np.all(workload == workload[0])
    assert len(set(workload[0])) == 3


def test_temporal_workload_is_reproducible_with_seed():
    first = generate_temporal_workload(8, 10, 3, 0.5, seed=42)
    second = generate_temporal_workload(8, 10, 3, 0.5, seed=42)

    np.testing.assert_array_equal(first, second)


def test_temporal_workload_rejects_dimension_larger_than_node_count():
    with pytest.raises(ValueError, match="dim cannot exceed num_nodes"):
        generate_temporal_workload(2, 1, 3, 0.5)
