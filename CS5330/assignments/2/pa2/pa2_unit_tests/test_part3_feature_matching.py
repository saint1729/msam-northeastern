#!/usr/bin/python3

import numpy as np


def test_compute_feature_distances_2d(compute_feature_distances):
    """
    Test feature distance calculations.
    """
    v0 = np.array([-2, 0]).reshape(1, 2)
    v1 = np.array([2, 0]).reshape(1, 2)
    v2 = np.array([4, 0]).reshape(1, 2)
    v3 = np.array([-4, 0]).reshape(1, 2)

    feats1 = np.vstack([v0.copy(), v1.copy(), v2.copy()])
    feats2 = np.vstack([v0.copy(), v1.copy(), v2.copy(), v3.copy()])

    inter_dists = compute_feature_distances(feats1, feats2)

    expected_distances = np.array([[0, 4, 6, 2], [4, 0, 2, 6], [6, 2, 0, 8]])

    assert inter_dists.shape[0] == 3
    assert inter_dists.shape[1] == 4
    assert np.allclose(inter_dists, expected_distances, atol=1e-03)


def test_compute_feature_distances_10d(compute_feature_distances):
    """ Check inter-feature distances for two 10-D vectors """

    v0 = np.zeros((1, 10))
    v1 = np.ones((1, 10))

    feats1 = np.vstack([v0.copy(), v1.copy()])
    feats2 = np.vstack([v1.copy(), v0.copy()])

    inter_dists = compute_feature_distances(feats1, feats2)

    # sqrt(1^2 + 1^2 + ... + 1^2) = sqrt(10)
    expected_inter_dists = np.array([[np.sqrt(10), 0], [0, np.sqrt(10)]])

    assert np.allclose(expected_inter_dists, inter_dists)


def test_match_features_ratio_test(match_features_ratio_test):
    """
    Few matches example. Match based on the following affinity/distance matrix:
    """
    feats1 = np.array([[0, 10], [10, 0]])  # Dist to feats2 = [[ 2.236,  1. ] [12.04, 13.453]]

    feats2 = np.array([[1, 8], [0, 9]])

    # Using NNDR as threshold
    # Since 1st point of feats2 fails the ratio test
    # Since 2nd point of feats2 passes the ratio test

    matches = np.array(
        [
            [0, 1],
        ]
    )

    result, confidences = match_features_ratio_test(feats1, feats2)

    assert np.array_equal(matches, result[np.argsort(result[:, 0])])
