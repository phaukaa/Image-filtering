import cv2
import time

def color2gray(image):
    """
    Function to turn image into grayscale using python
    param (numpy.ndarray): image
    return (numpy.ndarray): grayscaleimage (ndarray)
    """
    for i in range(len(image)):
        for j in range(len(image[i])):
            c1 = image[i, j, 0] * 0.07
            c2 = image[i, j, 1] * 0.72
            c3 = image[i, j, 2] * 0.21
            gray = (c1 + c2 + c3)
            image[i, j, 0] = gray
            image[i, j, 1] = gray
            image[i, j, 2] = gray
    return image

"""t1 = time.perf_counter()
filename = "rain.jpg"
image = cv2.imread(filename)
grayscaleimage = color2gray(image)
name = filename.split(".")[0]
ending = filename.split(".")[1]
grayscaleimage = grayscaleimage.astype("uint8")
cv2.imwrite("{}_grayscale.{}".format(name, ending), grayscaleimage)
t2 = time.perf_counter()
print("Time used: {}".format(t2-t1))"""
