from instapy.python_color2gray import color2gray as pg
from instapy.python_color2sepia import color2sepia as ps
from instapy.numpy_color2gray import color2gray as ng
from instapy.numpy_color2sepia import color2sepia as ns
from instapy.numba_color2gray import color2gray as bg
from instapy.numba_color2sepia import color2sepia as bs
import cv2


def grayscale_image(input_filename, output_filename=None, scale=1, implementation="numpy"):
    """
    Function to turn your inut file into a grayscale image
    param1 (str): til filename of the file you want to use the filter on
    param2 (str): the putput filename of the filtered image
            Default = None
            If no param is given, the image filename will be the same as the input file, with _{implementation}_grayscale ending
    param3 (float): the scale you want to scale your image to
            Default: 1
            I no param given, the output image will be the same size as the input
    param4 (str): the implementation (python, numpy, numba) you want to use to filter your image
            Default: numpy
            If no param given, the fucnction will use numpy to filter the image, since this is the fastest one of these three
    return (numpy.ndarray): the array of the image 
    """
    image = cv2.imread(input_filename)
    height = int(image.shape[0])
    width = int(image.shape[1])
    image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

    if implementation == "python":
        gray = pg(image)

    elif implementation == "numba":
        gray = bg(image)

    else:
        gray = ng(image)

    if output_filename:
        cv2.imwrite(output_filename, gray.astype("uint8"))
    else:
        filename = "{}_{}_grayscale.{}".format(
                input_filename.split(".")[0], implementation, input_filename.split(".")[1])
        cv2.imwrite(filename, gray.astype("uint8"))

    return gray


def sepia_image(input_filename, output_filename=None, scale=1, implementation="numpy"):
    """
    Function to turn your inut file into a sepia image
    param1 (str): til filename of the file you want to use the filter on
    param2 (str): the putput filename of the filtered image
            Default = None
            If no param is given, the image filename will be the same as the input file, with _{implementation}_sepia ending
    param3 (float): the scale you want to scale your image to
            Default: 1
            I no param given, the output image will be the same size as the input
    param4 (str): the implementation (python, numpy, numba) you want to use to filter your image
            Default: numpy
            If no param given, the fucnction will use numpy to filter the image, since this is the fastest one of these three
    return (numpy.ndarray): the array of the image 
    """
    image = cv2.imread(input_filename)
    height = int(image.shape[0])
    width = int(image.shape[1])
    image = cv2.resize(image, (0, 0), fx=scale, fy=scale)

    if implementation == "python":
        sepia = ps(image)

    elif implementation == "numba":
        sepia = bs(image)

    else:
        sepia = ns(image)

    if output_filename:
        cv2.imwrite(output_filename, sepia.astype("uint8"))
    else:
        filename = "{}_{}_sepia.{}".format(
            input_filename.split(".")[0], implementation, input_filename.split(".")[1])
        cv2.imwrite(filename, sepia.astype("uint8"))

    return image
