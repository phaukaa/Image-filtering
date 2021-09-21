import numpy as np
import time
import cv2

def color2gray(image):
    """
    Function to turn image into grayscale using numpy
    param (numpy.ndarray): image
    return (numpy.ndarray): grayscaleimage (ndarray)
    """
    gray = np.dot(image[..., :3], [0.07, 0.72, 0.21])
    return gray

"""t1 = time.perf_counter()
filename = "rain.jpg"
image = cv2.imread(filename)
imagematrix = color2gray(image)
name = filename.split(".")[0]
ending = filename.split(".")[1]
grayimage = imagematrix.astype("uint8")
cv2.imwrite("{}_grayscale.{}".format(name, ending), grayimage)
t2 = time.perf_counter()
print("Time used: {}".format(t2-t1))"""
