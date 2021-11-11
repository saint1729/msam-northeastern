import numpy as np
import cv2
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.axes._axes import Axes

from IPython.core.debugger import set_trace
from typing import Any, Callable, List, Tuple
    
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


def im2single(im):
    im = im.astype(np.float32) / 255
    return im


def single2im(im):
    im *= 255
    im = im.astype(np.uint8)
    return im


def load_image(path: str) -> np.ndarray:
    return cv2.imread(path)[:, :, ::-1]


def save_image(path, im):
    return cv2.imwrite(path, single2im(im.copy())[:, :, ::-1])


def evaluate_points(projection: Callable, P: np.ndarray, points_2d: np.ndarray, points_3d: np.ndarray) -> (np.ndarray, float):
    """Evaluate the residual between actual 2D points and the projected 2D
    points calculated from the projection matrix.

    You do not need to modify anything in this function, although you can if you
    want to.

    Args:
        M: a 3 x 4 numpy array representing the projection matrix.
        points_2d: a N x 2 numpy array representing the 2D points.
        points_3d: a N x 3 numpy array representing the 3D points.

    Returns:
        estimated_points_2d: a N x 2 numpy array representing the projected
            2D points
        residual: a float value representing the residual
    """

    points_3d = np.hstack((points_3d, np.ones((points_3d.shape[0], 1))))
    estimated_points_2d = projection(P, points_3d)

    residual = np.mean(np.hypot(estimated_points_2d[:, 0] - points_2d[:, 0],
        estimated_points_2d[:, 1] - points_2d[:, 1]))

    return estimated_points_2d, residual


def visualize_points_image(actual_pts: np.ndarray, projected_pts: np.ndarray, im_path: str) -> None:
    """Visualize the actual 2D points and the projected 2D points calculated
    from the projection matrix.

    You do not need to modify anything in this function, although you can if
    you want to.

    Args:
        actual_pts: a N x 2 numpy array representing the actual 2D points.
        projected_pts: a N x 2 numpy array representing the projected 2D points.
        im_path: a string representing the path to the image.

    Returns:
        None
    """

    im = load_image(im_path)
    _, ax = plt.subplots()

    ax.imshow(im)
    ax.scatter(actual_pts[:, 0], actual_pts[:, 1],
        c="red", marker="o", label="Actual points")
    ax.scatter(projected_pts[:, 0], projected_pts[:, 1],
        c="green", marker="+", label="Projected points")

    ax.legend()


def visualize_points(actual_pts: np.ndarray, projected_pts: np.ndarray) -> None:
    """Visualize the actual 2D points and the projected 2D points calculated
    from the projection matrix.

    You do not need to modify anything in this function, although you can if
    you want to.

    Args:
        actual_pts: a N x 2 numpy array representing the actual 2D points.
        projected_pts: a N x 2 numpy array representing the projected 2D points.

    Returns:
        None
    """
    _, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(actual_pts[:, 0], actual_pts[:, 1],
        c="red", marker="o", label="Actual points")
    ax.scatter(projected_pts[:, 0], projected_pts[:, 1],
        c="green", marker="+", label="Projected points")

    plt.ylim(max(plt.ylim()), min(plt.ylim()))
    ax.legend()
    ax.axis('equal')


def plot3dview_2_cameras(
    points_3d: np.ndarray, camera_center_1: np.ndarray, camera_center_2: np.ndarray, R1: np.ndarray, R2: np.ndarray
) -> None:
    """Visualize the actual 3D points and the estimated 3D camera center for
    2 cameras.

    You do not need to modify anything in this function, although you can if
    you want to.

    Args:
        points_3d: a N x 3 numpy array representing the actual 3D points
        camera_center_1: a 1 x 3 numpy array representing the first camera
            center
        camera_center_2: a 1 x 3 numpy array representing the second camera
            center
        R1: a 3 x 3 numpy array representing the rotation matrix for the first
            camera
        R2: a 3 x 3 numpy array representing the rotation matrix for the second
            camera

    Returns:
        None
    """

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
    ax.scatter(points_3d[:, 0], points_3d[:, 1], points_3d[:, 2],
        c="blue", marker="o", s=10, depthshade=0)

    camera_center_1 = camera_center_1.squeeze()
    ax.scatter(camera_center_1[0], camera_center_1[1], camera_center_1[2],
        c="red", marker="x", s=20, depthshade=0)

    camera_center_2 = camera_center_2.squeeze()
    ax.scatter(camera_center_2[0], camera_center_2[1], camera_center_2[2],
        c="red", marker="x", s=20, depthshade=0)

    v1 = R1[:, 0] * 5
    v2 = R1[:, 1] * 5
    v3 = R1[:, 2] * 5

    cc0, cc1, cc2 = camera_center_1

    ax.plot3D([0, 5], [0, 0], [0, 0], c="r")
    ax.plot3D([0, 0], [0, 5], [0, 0], c="g")
    ax.plot3D([0, 0], [0, 0], [0, 5], c="b")

    ax.plot3D([cc0, cc0 + v1[0]], [cc1, cc1 + v1[1]], [cc2, cc2 + v1[2]], c="r")
    ax.plot3D([cc0, cc0 + v2[0]], [cc1, cc1 + v2[1]], [cc2, cc2 + v2[2]], c="g")
    ax.plot3D([cc0, cc0 + v3[0]], [cc1, cc1 + v3[1]], [cc2, cc2 + v3[2]], c="b")

    v1 = R2[:, 0] * 5
    v2 = R2[:, 1] * 5
    v3 = R2[:, 2] * 5

    cc0, cc1, cc2 = camera_center_2

    ax.plot3D([0, 1], [0, 0], [0, 0], c="r")
    ax.plot3D([0, 0], [0, 1], [0, 0], c="g")
    ax.plot3D([0, 0], [0, 0], [0, 1], c="b")

    ax.plot3D([cc0, cc0 + v1[0]], [cc1, cc1 + v1[1]], [cc2, cc2 + v1[2]], c="r")
    ax.plot3D([cc0, cc0 + v2[0]], [cc1, cc1 + v2[1]], [cc2, cc2 + v2[2]], c="g")
    ax.plot3D([cc0, cc0 + v3[0]], [cc1, cc1 + v3[1]], [cc2, cc2 + v3[2]], c="b")

    # draw vertical lines connecting each point to ground
    min_z = min(points_3d[:, 2])
    for p in points_3d:
        x, y, z = p
        ax.plot3D(xs=[x, x], ys=[y, y], zs=[z, min_z], c="black", linewidth=1)

    x, y, z = camera_center_1
    ax.plot3D(xs=[x, x], ys=[y, y], zs=[z, min_z], c="black", linewidth=1)

    x, y, z = camera_center_2
    ax.plot3D(xs=[x, x], ys=[y, y], zs=[z, min_z], c="black", linewidth=1)


def plot3dview_with_coordinates(points_3d: np.ndarray, camera_center: np.ndarray, R: np.ndarray) -> None:
    """Visualize the actual 3D points and the estimated 3D camera center.

    You do not need to modify anything in this function, although you can if
    you want to.

    Args:
        points_3d: a N x 3 numpy array representing the actual 3D points.
        camera_center: a 1 x 3 numpy array representing the camera center.
        R: a 3 x 3 numpy array representing the rotation matrix for the camera.

    Returns:
        None
    """

    v1 = R[:, 0] * 5
    v2 = R[:, 1] * 5
    v3 = R[:, 2] * 5

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
    ax.scatter(points_3d[:, 0], points_3d[:, 1], points_3d[:, 2],
        c="blue", marker="o", s=10, depthshade=0)
    camera_center = camera_center.squeeze()
    ax.scatter(camera_center[0], camera_center[1], camera_center[2],
        c="red", marker="x", s=20, depthshade=0)

    cc0, cc1, cc2 = camera_center

    ax.plot3D([0, 5], [0, 0], [0, 0], c="r")
    ax.plot3D([0, 0], [0, 5], [0, 0], c="g")
    ax.plot3D([0, 0], [0, 0], [0, 5], c="b")

    ax.plot3D([cc0, cc0 + v1[0]], [cc1, cc1 + v1[1]], [cc2, cc2 + v1[2]], c="r")
    ax.plot3D([cc0, cc0 + v2[0]], [cc1, cc1 + v2[1]], [cc2, cc2 + v2[2]], c="g")
    ax.plot3D([cc0, cc0 + v3[0]], [cc1, cc1 + v3[1]], [cc2, cc2 + v3[2]], c="b")

    # draw vertical lines connecting each point to ground
    min_z = min(points_3d[:, 2])
    for p in points_3d:
        x, y, z = p
        ax.plot3D(xs=[x, x], ys=[y, y], zs=[z, min_z], c="black", linewidth=1)
    x, y, z = camera_center
    ax.plot3D(xs=[x, x], ys=[y, y], zs=[z, min_z], c="black", linewidth=1)


def plot3dview(points_3d: np.ndarray, camera_center: np.ndarray) -> None:
    """
    Visualize the actual 3D points and the estimated 3D camera center.

    You do not need to modify anything in this function, although you can if
    you want to.

    Args:
        points_3d: a N x 3 numpy array representing the actual 3D points.
        camera_center: a 1 x 3 numpy array representing the camera center.

    Returns:
        None
    """
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(111, projection="3d")
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
    ax.scatter(points_3d[:, 0], points_3d[:, 1], points_3d[:, 2],
        c="blue", marker="o", s=10, depthshade=0)
    camera_center = camera_center.squeeze()
    ax.scatter(camera_center[0], camera_center[1], camera_center[2],
        c="red", marker="x", s=20, depthshade=0)

    # draw vertical lines connecting each point to ground
    min_z = min(points_3d[:, 2])
    for p in points_3d:
        x, y, z = p
        ax.plot3D(xs=[x, x], ys=[y, y], zs=[z, min_z], c="black", linewidth=1)
    x, y, z = camera_center
    ax.plot3D(xs=[x, x], ys=[y, y], zs=[z, min_z], c="black", linewidth=1)

    set_axes_equal(ax)

    return ax


def draw_epipolar_lines(
    F: np.ndarray,
    img_left: np.ndarray,
    img_right: np.ndarray,
    pts_left: np.ndarray,
    pts_right: np.ndarray,
    figsize=(10, 8)
):
    """Draw the epipolar lines given the fundamental matrix, left right images
    and left right datapoints

    You do not need to modify anything in this function.

    Args:
        F: a 3 x 3 numpy array representing the fundamental matrix, such that
            p_right^T @ F @ p_left = 0 for correct correspondences
        img_left: array representing image 1.
        img_right: array representing image 2.
        pts_left: array of shape (N,2) representing image 1 datapoints.
        pts_right: array of shape (N,2) representing image 2 datapoints.

    Returns:
        None
    """
    # ------------ lines in the RIGHT image --------------------
    imgh_right, imgw_right = img_right.shape[:2]
    # corner points, as homogeneous (x,y,1)
    p_ul = np.asarray([0, 0, 1])
    p_ur = np.asarray([imgw_right, 0, 1])
    p_bl = np.asarray([0, imgh_right, 1])
    p_br = np.asarray([imgw_right, imgh_right, 1])

    # The equation of the line through two points
    # can be determined by taking the ‘cross product’
    # of their homogeneous coordinates.

    # left and right border lines, for the right image
    l_l = np.cross(p_ul, p_bl)
    l_r = np.cross(p_ur, p_br)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=figsize)

    ax[1].imshow(img_right)
    ax[1].autoscale(False)
    ax[1].scatter(pts_right[:, 0], pts_right[:, 1], marker='o', s=20, c='yellow',
        edgecolors='red')
    for p in pts_left:
        p = np.hstack((p, 1))[:, np.newaxis]
        # get defn of epipolar line in right image, corresponding to left point p
        l_e = np.dot(F, p).squeeze()
        # find where epipolar line in right image crosses the left and image borders
        p_l = np.cross(l_e, l_l)
        p_r = np.cross(l_e, l_r)
        # convert back from homogeneous to cartesian by dividing by 3rd entry
        # draw line between point on left border, and on the right border
        x = [p_l[0]/p_l[2], p_r[0]/p_r[2]]
        y = [p_l[1]/p_l[2], p_r[1]/p_r[2]]
        ax[1].plot(x, y, linewidth=1, c='blue')

    # ------------ lines in the LEFT image --------------------
    imgh_left, imgw_left = img_left.shape[:2]

    # corner points, as homogeneous (x,y,1)
    p_ul = np.asarray([0, 0, 1])
    p_ur = np.asarray([imgw_left, 0, 1])
    p_bl = np.asarray([0, imgh_left, 1])
    p_br = np.asarray([imgw_left, imgh_left, 1])

    # left and right border lines, for left image
    l_l = np.cross(p_ul, p_bl)
    l_r = np.cross(p_ur, p_br)

    ax[0].imshow(img_left)
    ax[0].autoscale(False)
    ax[0].scatter(pts_left[:, 0], pts_left[:, 1], marker='o', s=20, c='yellow',
        edgecolors='red')
    for p in pts_right:
        p = np.hstack((p, 1))[:, np.newaxis]
        # defn of epipolar line in the left image, corresponding to point p in the right image
        l_e = np.dot(F.T, p).squeeze()
        p_l = np.cross(l_e, l_l)
        p_r = np.cross(l_e, l_r)
        x = [p_l[0]/p_l[2], p_r[0]/p_r[2]]
        y = [p_l[1]/p_l[2], p_r[1]/p_r[2]]
        ax[0].plot(x, y, linewidth=1, c='blue')


def get_matches(pic_a: np.ndarray, pic_b: np.ndarray, n_feat: int) -> (np.ndarray, np.ndarray):
    """Get unreliable matching points between two images using SIFT.

    You do not need to modify anything in this function, although you can if
    you want to.

    Args:
        pic_a: a numpy array representing image 1.
        pic_b: a numpy array representing image 2.
        n_feat: an int representing number of matching points required.

    Returns:
        pts_a: a numpy array representing image 1 points.
        pts_b: a numpy array representing image 2 points.
    """
    pic_a = cv2.cvtColor(pic_a, cv2.COLOR_BGR2GRAY)
    pic_b = cv2.cvtColor(pic_b, cv2.COLOR_BGR2GRAY)

    try:
        sift = cv2.xfeatures2d.SIFT_create()
    except:
        sift = cv2.SIFT_create()

    kp_a, desc_a = sift.detectAndCompute(pic_a, None)
    kp_b, desc_b = sift.detectAndCompute(pic_b, None)
    dm = cv2.BFMatcher(cv2.NORM_L2)
    matches = dm.knnMatch(desc_b, desc_a, k=2)
    good_matches = []
    for m, n in matches:
        if m.distance / n.distance <= 0.8:
            good_matches.append(m)
    pts_a = []
    pts_b = []
    for m in good_matches[: int(n_feat)]:
        pts_a.append(kp_a[m.trainIdx].pt)
        pts_b.append(kp_b[m.queryIdx].pt)

    return np.asarray(pts_a), np.asarray(pts_b)


def hstack_images(imgA: np.ndarray, imgB: np.ndarray) -> np.ndarray:
    """Stacks 2 images side-by-side

    Args:
        imgA: a numpy array representing image 1.
        imgB: a numpy array representing image 2.

    Returns:
        img: a numpy array representing the images stacked side by side.
    """
    Height = max(imgA.shape[0], imgB.shape[0])
    Width = imgA.shape[1] + imgB.shape[1]

    newImg = np.zeros((Height, Width, 3), dtype=imgA.dtype)
    newImg[: imgA.shape[0], : imgA.shape[1], :] = imgA
    newImg[: imgB.shape[0], imgA.shape[1] :, :] = imgB

    return newImg


def show_correspondence2(
    imgA: np.ndarray, imgB: np.ndarray, X1: np.ndarray, Y1: np.ndarray, X2: np.ndarray, Y2: np.ndarray, line_colors=None
) -> None:
    """Visualizes corresponding points between two images. Corresponding points
    will have the same random color.

    Args:
        imgA: a numpy array representing image 1.
        imgB: a numpy array representing image 2.
        X1: a numpy array representing x coordinates of points from image 1.
        Y1: a numpy array representing y coordinates of points from image 1.
        X2: a numpy array representing x coordinates of points from image 2.
        Y2: a numpy array representing y coordinates of points from image 2.
        line_colors: a N x 3 numpy array containing colors of correspondence
            lines (optional)

    Returns:
        None
    """
    newImg = hstack_images(imgA, imgB)
    shiftX = imgA.shape[1]
    X1 = X1.astype(np.int)
    Y1 = Y1.astype(np.int)
    X2 = X2.astype(np.int)
    Y2 = Y2.astype(np.int)

    dot_colors = np.random.rand(len(X1), 3)
    if imgA.dtype == np.uint8:
        dot_colors *= 255
    if line_colors is None:
        line_colors = dot_colors

    for x1, y1, x2, y2, dot_color, line_color in zip(X1, Y1, X2, Y2, dot_colors, line_colors):
        newImg = cv2.circle(newImg, (x1, y1), 5, dot_color, -1)
        newImg = cv2.circle(newImg, (x2 + shiftX, y2), 5, dot_color, -1)
        newImg = cv2.line(newImg, (x1, y1), (x2 + shiftX, y2), line_color, 2, cv2.LINE_AA)

    return newImg


def set_axes_equal(ax: Axes) -> None:
    """
    Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Ref: https://github.com/borglab/gtsam/blob/develop/python/gtsam/utils/plot.py#L13

    Args:
        ax: axis for the plot.
    Returns:
        None
    """
    # get the min and max value for each of (x, y, z) axes as 3x2 matrix.
    # This gives us the bounds of the minimum volume cuboid encapsulating all
    # data.
    limits = np.array(
        [
            ax.get_xlim3d(),
            ax.get_ylim3d(),
            ax.get_zlim3d(),
        ]
    )

    # find the centroid of the cuboid
    centroid = np.mean(limits, axis=1)

    # pick the largest edge length for this cuboid
    largest_edge_length = np.max(np.abs(limits[:, 1] - limits[:, 0]))

    # set new limits to draw a cube using the largest edge length
    radius = 0.5 * largest_edge_length
    ax.set_xlim3d([centroid[0] - radius, centroid[0] + radius])
    ax.set_ylim3d([centroid[1] - radius, centroid[1] + radius])
    ax.set_zlim3d([centroid[2] - radius, centroid[2] + radius])
