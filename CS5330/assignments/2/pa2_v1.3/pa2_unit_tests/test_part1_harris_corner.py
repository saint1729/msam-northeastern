#!/usr/bin/python3

from typing import Any, Callable, List, Tuple

import numpy as np


def verify(function: Callable) -> str:
    """Will indicate with a print statement whether assertions passed or failed
    within function argument call.
    Args:
        function: Python function object
    Returns:
        string that is colored red or green when printed, indicating success
    """
    try:
        function
        return '\x1b[32m"Correct"\x1b[0m'
    except AssertionError:
        return '\x1b[31m"Wrong"\x1b[0m'


def test_compute_image_gradients(compute_image_gradients):
    #check image gradients with simple 7x7 image
    M = 7
    N = 7
    image_bw = np.array(
        [
            [0., 1., 0., 0., 0., 0., 0.],
            [1., 1., 1., 1., 1., 1., 1.],
            [0., 1., 0., 0., 0., 0., 0.],
            [0., 1., 0., 0., 0., 0., 0.],
            [0., 1., 0., 0., 1., 0., 0.],
            [0., 1., 0., 0., 1., 0., 0.],
            [0., 1., 0., 0., 0., 0., 0.]
        ]).astype(np.float32)

    Ix, Iy = compute_image_gradients(image_bw)
    
    expected_Ix = np.array(
        [
            [3., 0., -2., 0., 0., 0., -1.],
            [4., 0., -2., 0., 0., 0., -2.],
            [4., 0., -3., 0., 0., 0., -1.],
            [4., 0., -4., 1., 0., -1., 0.],
            [4., 0., -4., 3., 0., -3., 0.],
            [4., 0., -4., 3., 0., -3., 0.],
            [3., 0., -3., 1., 0., -1., 0.]
        ]).astype(np.float32)
    expected_Iy = np.array(
        [
            [3., 4., 4., 4., 4., 4., 3.],
            [0., 0., 0., 0., 0., 0., 0.],
            [-2., -2., -3., -4., -4., -4., -3.],
            [0., 0., 0., 1., 2., 1., 0.],
            [0., 0., 0., 1., 2., 1., 0.],
            [0., 0., 0., -1., -2., -1., 0.],
            [-1., -2., -1., -1., -2., -1., 0.]
        ]).astype(np.float32)
      
    assert np.allclose(Ix, expected_Ix), print('Ix:\n{}\n, expted_Ix:\n{}'.format(Ix, expected_Ix))
    assert np.allclose(Iy, expected_Iy)


def test_get_gaussian_kernel_2D_peak(get_gaussian_kernel_2D):
    """ Ensure peak of 2d kernel is at center, and dims are correct """
    ksize = 29
    sigma = 7
    kernel = get_gaussian_kernel_2D(ksize, sigma)

    assert isinstance(kernel, np.ndarray)
    # kernel = kernel.numpy()

    # generated Gaussian kernel should have odd dimensions
    assert kernel.shape[0] % 1 == 0
    assert kernel.shape[1] % 1 == 0
    assert kernel.ndim == 2

    center_row = kernel.shape[0] // 2
    center_col = kernel.shape[1] // 2

    coords = np.where(kernel == kernel.max())
    coords = np.array(coords).T

    # should be only 1 peak
    assert coords.shape == (1, 2), "Peak is not unique"
    assert coords[0, 0] == center_row, "Peak is not at center row"
    assert coords[0, 1] == center_col, "Peak is not at center column"


def test_get_gaussian_kernel_2D(get_gaussian_kernel_2D) -> None:
    """Verify values of inner 5x5 patch of 29x29 Gaussian kernel."""
    ksize = 29
    sigma = 7
    kernel = get_gaussian_kernel_2D(ksize, sigma)
    assert kernel.shape == (29, 29), "The kernel is not the correct size"

    # peak should be at center
    gt_kernel_crop = np.array(
        [
            [0.00324, 0.00334, 0.00337, 0.00334, 0.00324],
            [0.00334, 0.00344, 0.00348, 0.00344, 0.00334],
            [0.00337, 0.00348, 0.00351, 0.00348, 0.00337],
            [0.00334, 0.00344, 0.00348, 0.00344, 0.00334],
            [0.00324, 0.00334, 0.00337, 0.00334, 0.00324],
        ]
    )

    kernel_h, kernel_w = kernel.shape
    h_center = kernel_h // 2
    w_center = kernel_w // 2
    student_kernel_crop = kernel[h_center - 2 : h_center + 3, w_center - 2 : w_center + 3]

    assert np.allclose(gt_kernel_crop, student_kernel_crop, atol=1e-5), "Values dont match"
    assert np.allclose(kernel.sum(), np.array([1.]), atol=1e-3)



def test_get_gaussian_kernel_2D_sumsto1(get_gaussian_kernel_2D):
    """ Verifies that generated 2d Gaussian kernel sums to 1. """
    ksize = 29
    sigma = 7
    kernel = get_gaussian_kernel_2D(ksize, sigma)
    assert np.allclose(kernel.sum(), np.array([1.]), atol=1e-3), "Kernel doesnt sum to 1"

    
def test_second_moments(second_moments):
    #checks second moments using dummy image
    image_bw = dummy_image = np.array(
        [
            [1., 0., 0., 0., 0., 0., 1.],
            [0., 1., 0., 0., 0., 1., 0.],
            [0., 0., 1., 0., 1., 0., 0.],
            [0., 0., 0., 2., 0., 0., 0.],
            [0., 0., 1., 0., 1., 0., 0.],
            [0., 1., 1., 0., 0., 1., 0.],
            [1., 0., 0., 0., 0., 0., 1.],
        ]).astype(np.float32)
    ksize = 7
    sigma = 10
    sx2, sy2, sxsy = second_moments(image_bw, ksize, sigma)

    gt_sx2_crop = np.array([[1.5391557, 1.8679417, 2.0118287],
                            [1.9541941, 2.2874434, 2.506919 ],
                            [2.0641084, 2.4747922, 2.7155795]]).astype(np.float32)

    gt_sy2_crop = np.array([[1.9601676, 2.1796772, 1.9561074],
                            [2.4648497, 2.7024632, 2.4535522],
                            [2.250107 , 2.4673026, 2.2386072]]).astype(np.float32)

    gt_sxsy_crop = np.array([[0.13332403, 0.20079066, 0.266298  ],
                             [0.3010661 , 0.28707492, 0.27026486],
                             [0.33388686, 0.33304197, 0.32891643]]).astype(np.float32)

    assert np.allclose(sx2[1:4,1:4], gt_sx2_crop, atol=1e-3)
    assert np.allclose(sy2[2:5,2:5], gt_sy2_crop, atol=1e-3)
    assert np.allclose(sxsy[1:4,2:5], gt_sxsy_crop, atol=1e-3)


def test_compute_harris_response_map(compute_harris_response_map):
    """ """
    image_bw = np.array(
        [
            [1., 0., 0., 0., 0., 0., 1.],
            [0., 1., 0., 0., 0., 1., 0.],
            [0., 0., 1., 0., 1., 0., 0.],
            [0., 0., 0., 1., 0., 0., 0.],
            [0., 0., 1., 0., 1., 0., 0.],
            [0., 1., 0., 0., 0., 1., 0.],
            [1., 0., 0., 0., 0., 0., 1.]
        ]).astype(np.float32)

    ksize = 7
    sigma = 5
    alpha = 0.05

    R = compute_harris_response_map(image_bw, ksize, sigma, alpha)
  
    # peak at the "X" in the center
    expected_R = np.array(
        [
            [0.1, 0.3, 0.7, 0.9, 0.7, 0.3, 0.1],
            [0.3, 0.6, 1.1, 1.3, 1.1, 0.6, 0.3],
            [0.7, 1.1, 1.7, 2.2, 1.7, 1.1, 0.7],
            [0.9, 1.3, 2.2, 2.8, 2.2, 1.3, 0.9],
            [0.7, 1.1, 1.7, 2.2, 1.7, 1.1, 0.7],
            [0.3, 0.6, 1.1, 1.3, 1.1, 0.6, 0.3],
            [0.1, 0.3, 0.7, 0.9, 0.7, 0.3, 0.1]
        ], dtype=np.float32)

    assert np.allclose(R, expected_R, atol=0.1)


def test_nms_maxpool(nms_maxpool):
    """ """

    R = np.array(
    [
        [1,2,2,1,2],
        [1,6,2,1,1],
        [2,2,1,1,1],
        [1,1,1,7,1],
        [1,1,1,1,1]
    ]).astype(np.float32)

    k = 2
    ksize = 3

    x, y, c = nms_maxpool(R, ksize, k)

    expected_x = np.array([3,1])
    expected_y = np.array([3,1])

    assert np.allclose(x, expected_x)
    assert np.allclose(y, expected_y)
    assert c.size == 2

def test_remove_border_vals(remove_border_vals):
    #test proper removal of border corners
    M = 16
    N = 16
    k = 256

    dummy_image = np.array(
        [
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]
        ]).astype(np.float32)
    inds = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    #x, y contain every index of the dummy image
    x = np.tile(inds, (16, 1))
    y = x.T
    c = x + y

    x, y, c = remove_border_vals(dummy_image, x.flatten(), y.flatten(), c.flatten())

    #only the index 7,7 is valid  to create a 16x16 window
    gt_x = np.array([7])
    gt_y = np.array([7])
    gt_c = np.array([14])

    assert np.allclose(x, gt_x)
    assert np.allclose(y, gt_y)
    assert np.allclose(c, gt_c)



def test_get_harris_interest_points(get_harris_interest_points):
    """
    Tests that get_interest_points function can get the correct coordinate. 
    """    
    dummy_image = np.array(
        [
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
            [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
            [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
            [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
            [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 0., 2., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
            [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
            [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
            [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
            [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]
        ]).astype(np.float32)

    k = 1

    x, y, confidences = get_harris_interest_points(dummy_image, k)
    
    # interest point at (9,9)
    expected_x = np.array([9])
    expected_y = np.array([9])
    expected_confidences = np.array([4.80069923])

    assert np.allclose(expected_x, x)
    assert np.allclose(expected_y, y)
    assert np.allclose(expected_confidences, confidences), [expected_confidences, confidences]






