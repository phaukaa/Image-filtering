import pytest
import importlib
import numpy as np
import random
import cv2

import instapy
from instapy import grayscale_image, sepia_image


def isGray(image):
    """
    Heo function to check if a given image is grayscale
    param (numpy.ndarray): image
    return: True or False 
    """
    if(len(image.shape) < 3):
        return True
    b, g, r = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    if (b == g).all() and (b == r).all():
        return True
    return False

@pytest.mark.parametrize("implementation", ("python_color2gray", "numpy_color2gray", "numba_color2gray"))
def test_grayscale_filter(implementation):
    """
    Function to test if an image is grayscale using pytest
    param: pytest.mark.parametrize
    The function tests color2gray function in all given params in pytest.mark.parametrize using a random generated 3d array as image
    Asserts if the image is gray (as expected)
    """
    mod = importlib.import_module(f"instapy.{implementation}")
    grayimage = getattr(mod, "color2gray")
    image = np.random.randint(0, 255, size=(50, 50, 3))
    result = grayimage(image)
    assert isGray(result)
    n = random.randint(0, 49)
    gray = (image[n, n, 0] * 0.07 + image[n, n, 1] * 0.72 + image[n, n, 2] * 0.21)
    if len(result.shape) == 3:
        assert result[n, n, 0] == pytest.approx(gray, 0.1)
    else:
        assert result[n, n] == pytest.approx(gray, 0.1)

def isSepia(image, result):
    #Shows incorrect when using python/numba
    """
    Help function to check if given image is sepia (equal to expected image we know is sepia)
    param1: non-filtered image
    param2: sepia image
    return: if the sepia image is equal to epected image
    """
    sepiamatrix = np.array([[0.393, 0.769, 0.189],
                   [0.349, 0.686, 0.168],
                   [0.272, 0.534, 0.131]])

    n = random.randint(0, 49)

    bgrMatrix = sepiamatrix[::-1]

    sepiaimage = image.dot(bgrMatrix.T)
    sepiaimage[np.where(sepiaimage > 255)] = 255

    return result[n, n, 0] == sepiaimage[n, n, 0] and result[n, n, 1] == sepiaimage[n, n, 1] and result[n, n, 2] == sepiaimage[n, n, 2]

@pytest.mark.parametrize("implementation", ("python_color2sepia", "numpy_color2sepia", "numba_color2sepia"))
def test_sepia_filter(implementation):
    """
    Function to test if an image is sepia using pytest
    param: pytest.mark.parametrize
    The function tests color2sepia function in all given params in pytest.mark.parametrize using a random generated 3d array as image
    Asserts if the image is sepia (as expected)
    """
    mod = importlib.import_module(f"instapy.{implementation}")
    sepiaimage = getattr(mod, "color2sepia")
    image = np.random.randint(0, 255, size=(50, 50, 3))
    result = sepiaimage(image)

    assert isSepia(image, result)
    

# def test_init():
#     """
#     Tests if the init-functions grayscale_image and sepia_image are correct
#     Also creates a gray and sepia version of the rain.jpg image 
#     """
#     gray = grayscale_image("rain.jpg")
#     sepia = sepia_image("rain.jpg")
#     assert isGray(gray)
#     assert isSepia(cv2.imread("rain.jpg"), sepia)
