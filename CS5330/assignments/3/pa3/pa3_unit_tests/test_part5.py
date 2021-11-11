import pytest
import numpy as np
import logging
import cv2
from pathlib import Path

def test_get_emat_from_fmat(get_emat_from_fmat):
    F = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    K1 = np.array([
        [0.1, 0, 0],
        [0, 0.1, 0],
        [0, 0, 1]
    ])
    
    K2 = np.array([
        [10, 1, 0.5],
        [0, 10, -0.5],
        [0, 0, 1]
    ])
    
    expected_E = np.array([
        [ 1.,    2.,   30.  ],
        [ 4.1,   5.2,  63.  ],
        [ 0.55,  0.65,  7.5 ]
    ])
    
    E = get_emat_from_fmat(F, K1, K2)
    
    assert np.allclose(E, expected_E, atol=1e-2)