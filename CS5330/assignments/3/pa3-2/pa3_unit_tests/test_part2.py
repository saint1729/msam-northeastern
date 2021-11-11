"""Unit tests for fundamental_matrix module."""

from pathlib import Path
import math
import unittest

import numpy as np

DATA_ROOT = Path(__file__).resolve().parent.parent / "data"


def test_estimate_fundamental_matrix(estimate_fundamental_matrix):
    """Test whether student's fundamental matrix is correct

    Checks the student's implementation against the properties of the fundamental matrix
    """
    points1 = np.array(
        [
            [886.0, 347.0],
            [943.0, 128.0],
            [476.0, 590.0],
            [419.0, 214.0],
            [783.0, 521.0],
            [235.0, 427.0],
            [665.0, 429.0],
            [525.0, 234.0],
        ],
        dtype=np.float32,
    )

    points2 = np.array(
        [
            [903.0, 342.0],
            [867.0, 177.0],
            [958.0, 572.0],
            [328.0, 244.0],
            [1064.0, 470.0],
            [480.0, 495.0],
            [964.0, 419.0],
            [465.0, 263.0],
        ],
        dtype=np.float32,
    )

    F_student = estimate_fundamental_matrix(points1, points2)

    # Check Matrix is Rank 2
    assert np.linalg.matrix_rank(F_student) == 2, "Matrix is not rank 2"

    # Check values of Fundamental matrix    
    F_estimated = np.array([
        [-0.000000106713477,   0.000001502372207,  -0.000376414655535],
        [0.000001303817495,  -0.000000102651874,   0.003154174766710],
        [-0.000091649554798,  -0.004500733703440,   0.135109155020156]
    ], dtype=np.float32,)

    # Check estimated matrix up to scale ambiguity
    F_estimated /= F_student[2, 2]
    F_student /= F_student[2, 2]

    assert np.allclose(F_student, F_estimated, atol=1e-2), "Fundamental Matrices don't Match"


def test_normalize_points(normalize_points):
    """
    Test the normalization of points that will be used to estimate the
    fundamental matrix. Uses 8 points, and a 0-mean and unit variance
    normalization scheme.
    """

    # points to normalize
    points_input = np.array(
        [[-4, 64, 1], 
         [-3, 49, 1], 
         [-2, 36, 1], 
         [-1, 25, 1], 
         [0, 16, 1], 
         [1, 9, 1], 
         [2, 4, 1], 
         [3, 1, 1]
        ])

    # result of normalization
    expected_normalized_points = np.array(
        [
            [-0.27107076,  2.98177834,  1.        ],
            [-0.19362197,  1.82004652,  1.        ],
            [-0.11617318,  0.81321227,  1.        ],
            [-0.03872439, -0.03872439,  1.        ],
            [ 0.03872439, -0.73576349,  1.        ],
            [ 0.11617318, -1.277905,    1.        ],
            [ 0.19362197, -1.66514894,  1.        ],
            [ 0.27107076, -1.8974953,   1.        ],
        ]
    )

    # transformation matrix to achieve normalization
    expected_T = np.array([
        [ 0.07744879,  0.,          0.03872439],
        [ 0.,          0.07744879, -1.97494409],
        [ 0.,          0.,          1.        ]
    ])

    student_normalized_points, student_T = normalize_points(points_input)

    assert np.allclose(expected_normalized_points, student_normalized_points, atol=1e-2)

    assert np.allclose(expected_T, student_T, atol=1e-2)


def test_unnormalize_F(unnormalize_F):
    """
    Tests the de-normalization of the fundamental matrix
    once it has been estimated using normalized coordinates.
    Uses contrived matrices to be more interpretable.
    """

    F = np.array([[1, 2, 3], [1, 3, -1], [-2, 1, -1]])

    T_a = np.array([[1, 0, 2], [0, 2, -1], [0, 0, 1]])

    T_b = np.array([[2, 0, -1], [0, -1, 2], [0, 0, 1]])

    expected_unnormalized_F = np.array([[2, 8, 6], [-1, -6, 2], [-1, 10, -13]])

    student_unnormalized_F = unnormalize_F(F, T_a, T_b)

    assert np.allclose(expected_unnormalized_F, student_unnormalized_F, atol=1e-2)
