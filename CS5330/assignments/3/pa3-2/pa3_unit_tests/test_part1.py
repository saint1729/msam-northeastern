#!/usr/bin/python3

import numpy as np
from pathlib import Path

DATA_ROOT = Path(__file__).resolve().parent.parent / "data"


def test_projection(projection) -> None:
    """Test projection of 4 points into an image.

    Assume +z goes out of the camera, +x is to the right, and +y is downwards
    """
    # focal lengths are 1000 px, and (px,py) = (2000,1000)
    K = np.array([[1000, 0, 2000], [0, 1000, 1000], [0, 0, 1]])
    cTw = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])

    M = K @ cTw

    # (x,y,z, w) tuples
    # assume all points are in front of the camera (z>0)
    points_3d = np.array(
        [
            [1, 2, 5, 1],
            [1, 2, 6, 1],
            [-1, 2, 7, 1],
            [-1, 2, 8, 1],
        ]
    )

    points_2d = projection(M, points_3d)

    # all points should be below image center at (u,v)=(2000,1000) because y is positive
    expected_points_2d = np.array(
        [
            [2200, 1400],  # to the right of image center, since x>0
            [2167, 1333],  # farther away than 0th point -> so image center than point 0
            [1857, 1286],  # should be to the left of the points above, since x<0
            [1875, 1250],  # farther away than point 2 -> so closer to image center
        ]
    )
    assert np.allclose(points_2d, expected_points_2d, atol=1)


def test_calculate_camera_center(calculate_camera_center):
    """
    tests whether projection was implemented correctly
    """

    test_input = np.array(
        [
            [122.43413524, -58.4445669, -8.71785439, 1637.28675475],
            [4.54429487, 3.30940264, -134.40907701, 2880.869899],
            [0.02429085, 0.02388273, -0.01160657, 1.0],
        ]
    )

    test_cc = np.array([-18.27559442, -13.32677465, 20.48757872])

    cc = calculate_camera_center(test_input)

    assert cc.shape == test_cc.shape

    assert np.allclose(test_cc, cc, atol=1e-2)


def test_calculate_projection_matrix(calculate_projection_matrix):
    """
    tests whether camera matrix estimation is done correctly
    given an initial guess
    """

    pts2d_path = f"{DATA_ROOT}/CCB_GaTech/pts2d-pic_b.txt"
    pts3d_path = f"{DATA_ROOT}/CCB_GaTech/pts3d.txt"

    points_2d = np.loadtxt(pts2d_path)
    points_3d = np.loadtxt(pts3d_path)

    test_P_row = np.array([-0.45680404, -0.30239205, 2.0, 166.03023966])

    P = calculate_projection_matrix(points_2d, points_3d)
    # resolve scale ambiguity
    P /= P[2, 3]

    assert np.allclose(P[1, :], test_P_row, atol=1)
