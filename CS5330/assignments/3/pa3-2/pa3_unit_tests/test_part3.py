import pytest
import numpy as np
import logging
import cv2
from pathlib import Path

from pa3_code.utils import load_image, get_matches

DATA_ROOT = Path(__file__).resolve().parent.parent / "data"


def test_calculate_num_ransac_iterations(calculate_num_ransac_iterations):
    data_set = [
        (0.99, 1, 0.99, 1),
        (0.99, 10, 0.9, 11),
        (0.9, 15, 0.5, 75450),
        (0.95, 5, 0.66, 22),
    ]

    for prob_success, sample_size, ind_prob, num_samples in data_set:
        S = calculate_num_ransac_iterations(prob_success, sample_size, ind_prob)
        # print('ours: {}, gt: {}'.format(S, num_samples))
        assert pytest.approx(num_samples, abs=1.0) == S


def test_ransac_fundamental_matrix(ransac_fundamental_matrix):
    np.random.seed(0)
    pic_a = load_image(f"{DATA_ROOT}/argoverse_log_273c1883/ring_front_center_315975640448534784.jpg")
    scale_a = 0.5
    pic_b = load_image(f"{DATA_ROOT}/argoverse_log_273c1883/ring_front_center_315975643412234000.jpg")
    scale_b = 0.5
    n_feat = 4e3
    pic_a = cv2.resize(pic_a, None, fx=scale_a, fy=scale_a)
    pic_b = cv2.resize(pic_b, None, fx=scale_b, fy=scale_b)
    points_2d_pic_a, points_2d_pic_b = get_matches(pic_a, pic_b, n_feat)
    
    # insert gt correspondences
    gt_points_a, gt_points_b = np.load(f"{DATA_ROOT}/argoverse_log_273c1883/gt_corrs.npy")
    gt_points_a = gt_points_a / 2
    gt_points_b = gt_points_b / 2
    
    rand_idxes = np.random.choice(points_2d_pic_a.shape[0], 10)    
    points_2d_pic_a = np.vstack((points_2d_pic_a[rand_idxes], gt_points_a))
    points_2d_pic_b = np.vstack((points_2d_pic_b[rand_idxes], gt_points_b))   
    
    F, _, _ = ransac_fundamental_matrix(points_2d_pic_a, points_2d_pic_b)
    expected_F = np.array([
        [ 9.47482807e-07,  5.32561639e-05, -1.68859968e-02],
        [-5.47038098e-05,  1.43578556e-06,  3.43169296e-02],
        [ 1.62762452e-02, -1.18041151e-02, -6.73175964e+00]
    ])

    expected_F = expected_F / expected_F[2, 2]
    F = F / F[2, 2]
    # print('dist: {}'.format(np.mean(np.abs(expected_F - F))))

    assert np.allclose(F, expected_F, atol=1e-2)
