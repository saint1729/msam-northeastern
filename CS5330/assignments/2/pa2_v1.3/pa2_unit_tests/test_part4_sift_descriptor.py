#!/usr/bin/python3

import copy
import pdb
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from pa2_code.utils import load_image, evaluate_correspondence, rgb2gray, PIL_resize

ROOT = Path(__file__).resolve().parent.parent  # ../..


def test_get_magnitudes_and_orientations(get_magnitudes_and_orientations):
    """ Verify gradient magnitudes and orientations are computed correctly"""
    Ix = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    Iy = np.array([[0, 0, 0], [1, 1, 1], [1, 1, 1]])
    magnitudes, orientations = get_magnitudes_and_orientations(Ix, Iy)

    # there are 3 vectors -- (1,0) at 0 deg, (0,1) at 90 deg, and (-1,1) and 135 deg
    expected_magnitudes = np.array([[1, 1, 1], [1, 1, 1], [np.sqrt(2), np.sqrt(2), np.sqrt(2)]])
    expected_orientations = np.array(
        [[0, 0, 0], [np.pi / 2, np.pi / 2, np.pi / 2], [3 * np.pi / 4, 3 * np.pi / 4, 3 * np.pi / 4]]
    )

    assert np.allclose(magnitudes, expected_magnitudes)
    assert np.allclose(orientations, expected_orientations)


def test_get_gradient_histogram_vec_from_patch(get_gradient_histogram_vec_from_patch):
    """ Check if weighted gradient histogram is computed correctly """
    window_magnitudes = np.array(
        [
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
            [2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
            [2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
            [2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        ]
    )

    PI = np.pi
    window_orientations = np.array(
        [
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
        ]
    )

    wgh = get_gradient_histogram_vec_from_patch(window_magnitudes, window_orientations)

    expected_wgh = np.array(
        [
            [0.0, 0.0, 0.0, 0.0, 16.0, 0.0, 0.0, 0.0],  # magnitude was 1s
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],  # magnitude was 0s
            [0.0, 0.0, 0.0, 0.0, 16.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 32.0, 0.0, 0.0, 0.0],  # magnitude was 2s
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 16.0],
            [0.0, 0.0, 0.0, 0.0, 32.0, 0.0, 0.0, 0.0],  # magnitude was 2s
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 16.0],
            [0.0, 0.0, 0.0, 0.0, 16.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 16.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 16.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 16.0],
            [0.0, 0.0, 0.0, 0.0, 16.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 16.0],
        ]
    ).reshape(128, 1)

    assert np.allclose(wgh, expected_wgh, atol=1e-1)


def test_get_feat_vec(get_feat_vec):
    """ Check if feature vector for a specific interest point is returned correctly """
    window_magnitudes = np.array(
        [
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
            [2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
            [2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
            [2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        ]
    )

    PI = np.pi
    window_orientations = np.array(
        [
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
            [0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI, 0.0, 0.0, 0.0, 0.0, PI, PI, PI, PI],
        ]
    )

    feature_width = 16

    x, y = 7, 7

    fv = get_feat_vec(x, y, window_magnitudes, window_orientations, feature_width)

    expected_fv = np.array(
        [
            [0.0, 0.0, 0.0, 0.0, 0.485, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.485, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.687, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.485],
            [0.0, 0.0, 0.0, 0.0, 0.687, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.485],
            [0.0, 0.0, 0.0, 0.0, 0.485, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.485, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.485, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.485],
            [0.0, 0.0, 0.0, 0.0, 0.485, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.485],
        ]
    ).reshape(128, 1)

    assert np.allclose(fv, expected_fv, atol=1e-1)


def test_get_SIFT_descriptors(get_SIFT_descriptors):
    """ Check if the 128-d SIFT feature vector computed at each of the input points is returned correctly """

    image1 = np.array(
        [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
            [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
            [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
            [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
            [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
            [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
            [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
            [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
            [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
            [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
            [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
            [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
            [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34],
        ]
    ).astype(np.float32)

    X1, Y1 = np.array([8, 9]), np.array([8, 9])

    SIFT_descriptors = get_SIFT_descriptors(image1, X1, Y1)

    expected_SIFT_descriptors = np.array(
        [
            [
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
            ],
            [
                [0., 0., 0., 0., 0., 0.37945204, 0., 0.],
                [0., 0., 0., 0., 0., 0.37945204,  0., 0.],
                [0., 0., 0., 0., 0., 0.37945204,  0., 0.],
                [0., 0., 0., 0., 0., 0.32861511,  0., 0.49890103],
                [0., 0., 0., 0., 0., 0.37945204,  0., 0.],
                [0., 0., 0., 0., 0., 0.37945204,  0., 0.],
                [0., 0., 0., 0., 0., 0.37945204,  0., 0.],
                [0., 0., 0., 0., 0., 0.32861511,  0., 0.54743281],
                [0., 0., 0., 0., 0., 0.37945204,  0., 0.],
                [0., 0., 0., 0., 0., 0.37945204,  0., 0.],
                [0., 0., 0., 0., 0., 0.37945204,  0., 0.],
                [0., 0., 0., 0., 0., 0.32861511,  0., 0.59203022],
                [0., 0., 0.49890103, 0., 0., 0.32861532,  0., 0.        ],
                [0., 0., 0.54743281, 0., 0., 0.32861532,  0., 0.        ],
                [0., 0., 0.59203022, 0., 0., 0.32861532,  0., 0.        ],
                [0.33202056, 0., 0.54427702, 0., 0., 0.28458921,  0., 0.54427704],
            ]
        ]
    ).reshape(2, 128)

    assert np.allclose(SIFT_descriptors, expected_SIFT_descriptors, atol=1e-1)

def test_feature_matching_speed(get_harris_interest_points, match_features_ratio_test, get_SIFT_descriptors):
    """
    Test how long feature matching takes to execute on the Notre Dame pair.
    This unit test must run in under 90 seconds.
    """
    start = time.time()
    image1 = load_image(f"{ROOT}/data/1a_notredame.jpg")
    image2 = load_image(f"{ROOT}/data/1b_notredame.jpg")
    eval_file = f"{ROOT}/ground_truth/notredame.pkl"
    scale_factor = 0.5
    image1 = PIL_resize(image1, (int(image1.shape[1] * scale_factor), int(image1.shape[0] * scale_factor)))
    image2 = PIL_resize(image2, (int(image2.shape[1] * scale_factor), int(image2.shape[0] * scale_factor)))
    image1_bw = rgb2gray(image1)
    image2_bw = rgb2gray(image2)

    X1, Y1, _ = get_harris_interest_points(copy.deepcopy(image1_bw))
    X2, Y2, _ = get_harris_interest_points(copy.deepcopy(image2_bw))

    image1_features = get_SIFT_descriptors(image1_bw, X1, Y1)
    image2_features = get_SIFT_descriptors(image2_bw, X2, Y2)

    matches, confidences = match_features_ratio_test(image1_features, image2_features)
    print("{:d} matches from {:d} corners".format(len(matches), len(X1)))

    end = time.time()
    duration = end - start
    print(f"Your Feature matching pipeline takes {duration:.2f} seconds to run on Notre Dame")

    MAX_ALLOWED_TIME = 90  # sec
    assert duration < MAX_ALLOWED_TIME


def test_feature_matching_accuracy(get_harris_interest_points, match_features_ratio_test, get_SIFT_descriptors):
    """
    Test how long feature matching takes to execute on the Notre Dame pair.
    This unit test must achieve at least 80% accuracy.
    """
    image1 = load_image(f"{ROOT}/data/1a_notredame.jpg")
    image2 = load_image(f"{ROOT}/data/1b_notredame.jpg")
    eval_file = f"{ROOT}/ground_truth/notredame.pkl"
    scale_factor = 0.5
    image1 = PIL_resize(image1, (int(image1.shape[1] * scale_factor), int(image1.shape[0] * scale_factor)))
    image2 = PIL_resize(image2, (int(image2.shape[1] * scale_factor), int(image2.shape[0] * scale_factor)))
    image1_bw = rgb2gray(image1)
    image2_bw = rgb2gray(image2)

    X1, Y1, _ = get_harris_interest_points(copy.deepcopy(image1_bw))
    X2, Y2, _ = get_harris_interest_points(copy.deepcopy(image2_bw))

    image1_features = get_SIFT_descriptors(image1_bw, X1, Y1)
    image2_features = get_SIFT_descriptors(image2_bw, X2, Y2)

    matches, confidences = match_features_ratio_test(image1_features, image2_features)

    acc, _ = evaluate_correspondence(
        image1,
        image2,
        eval_file,
        scale_factor,
        X1[matches[:, 0]],
        Y1[matches[:, 0]],
        X2[matches[:, 1]],
        Y2[matches[:, 1]],
    )

    print(f"Your Feature matching pipeline achieved {100 * acc:.2f}% accuracy to run on Notre Dame")

    MIN_ALLOWED_ACC = 0.80  # 80 percent
    assert acc > MIN_ALLOWED_ACC


def test_extra_credit_vectorized_sift(get_harris_interest_points, match_features_ratio_test, get_sift_features_vectorized):
    """
    Test how long feature matching takes to execute on the Notre Dame pair.
    This unit test must run in under 90 seconds.
    """

    image1 = load_image(f"{ROOT}/data/1a_notredame.jpg")
    image2 = load_image(f"{ROOT}/data/1b_notredame.jpg")
    eval_file = f"{ROOT}/ground_truth/notredame.pkl"
    scale_factor = 0.5
    image1 = PIL_resize(image1, (int(image1.shape[1] * scale_factor), int(image1.shape[0] * scale_factor)))
    image2 = PIL_resize(image2, (int(image2.shape[1] * scale_factor), int(image2.shape[0] * scale_factor)))
    image1_bw = rgb2gray(image1)
    image2_bw = rgb2gray(image2)

    X1, Y1, _ = get_harris_interest_points(copy.deepcopy(image1_bw))
    X2, Y2, _ = get_harris_interest_points(copy.deepcopy(image2_bw))

    start = time.time()
    image1_features = get_sift_features_vectorized(image1_bw, X1, Y1)
    image2_features = get_sift_features_vectorized(image2_bw, X2, Y2)
    end = time.time()
    duration = end - start
    print(f"Your vectorized SIFT implementation takes {duration:.2f} seconds to run on Notre Dame")

    MAX_ALLOWED_TIME = 5  # sec
    assert duration < MAX_ALLOWED_TIME, "Runtime too long"

    matches, confidences = match_features_ratio_test(image1_features, image2_features)
    print("{:d} matches from {:d} corners".format(len(matches), len(X1)))

    acc, _ = evaluate_correspondence(
        image1,
        image2,
        eval_file,
        scale_factor,
        X1[matches[:, 0]],
        Y1[matches[:, 0]],
        X2[matches[:, 1]],
        Y2[matches[:, 1]],
    )
    print(f"Your vectorized feature matching pipeline achieved {100 * acc:.2f}% accuracy to run on Notre Dame")

    MIN_ALLOWED_ACC = 0.80  # 80 percent
    assert acc > MIN_ALLOWED_ACC, "Accuracy too low"
