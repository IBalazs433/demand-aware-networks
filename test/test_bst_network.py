import pytest

from src.networks.bst_network import BinarySearchTreeNetwork


@pytest.fixture
def network():
    result = BinarySearchTreeNetwork()
    for key in (10, 5, 15, 3, 7, 12, 18):
        result.insert(key)
    return result


def test_insert_and_search_report_node_and_depth(network):
    node, depth = network.search(7)

    assert node.key == 7
    assert depth == 2


def test_search_missing_key_reports_none_and_insertion_depth(network):
    node, depth = network.search(6)

    assert node is None
    assert depth == 3


@pytest.mark.parametrize(
    ("sender", "receiver", "expected_distance"),
    [
        (3, 7, 2),
        (3, 15, 3),
        (10, 10, 0),
        (5, 12, 3),
    ],
)
def test_request_returns_path_length_and_accumulates_cost(
    network, sender, receiver, expected_distance
):
    assert network.request(sender, receiver) == expected_distance
    assert network.communication_cost == expected_distance


def test_request_with_missing_node_returns_none_without_changing_cost(network):
    assert network.request(3, 99) is None
    assert network.communication_cost == 0


def test_lca_returns_common_ancestor_and_its_depth(network):
    ancestor, depth = network._lca(3, 7)

    assert ancestor.key == 5
    assert depth == 1
