import cv2
import time
from numba import jit

@jit
def color2sepia(image, sepiagrade=1):
    """
    Function to turn image into sepia using numba
    param1 (numpy.ndarray): image
    param2 (optional) (float): the grade of which you want to apply sepia filter
                                100% = 1, 0% = 0
                                default: 1
    return (numpy.ndarray): grayscaleimage (ndarray)
    """
    sepiamatrix = [[0.393 + 0.607 * (1 - sepiagrade), 
                    0.769 - 0.769 * (1 - sepiagrade), 
                    0.189 - 0.189 * (1 - sepiagrade)],
                   [0.349 - 0.349 * (1 - sepiagrade), 
                    0.686 + 0.314 * (1 - sepiagrade), 
                    0.168 - 0.168 * (1 - sepiagrade)],
                   [0.272 - 0.349 * (1 - sepiagrade), 
                    0.534 - 0.534 * (1 - sepiagrade), 
                    0.131 + 0.869 * (1 - sepiagrade)]]

    for i in range(len(image)):
        for j in range(len(image[i])):
            r = (image[i][j][2] * sepiamatrix[0][0] +
                 image[i][j][1] * sepiamatrix[0][1] +
                 image[i][j][0] * sepiamatrix[0][2])
            g = (image[i][j][2] * sepiamatrix[1][0] +
                 image[i][j][1] * sepiamatrix[1][1] +
                 image[i][j][0] * sepiamatrix[1][2])
            b = (image[i][j][2] * sepiamatrix[2][0] +
                 image[i][j][1] * sepiamatrix[2][1] +
                 image[i][j][0] * sepiamatrix[2][2])
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            image[i, j, 0] = b
            image[i, j, 1] = g
            image[i, j, 2] = r
    return image

"""t1 = time.perf_counter()
filename = "rain.jpg"
image = cv2.imread(filename)
sepiaImage = color2sepia(image)
name = filename.split(".")[0]
ending = filename.split(".")[1]
sepiaImage = sepiaImage.astype("uint8")
cv2.imwrite("{}_sepia.{}".format(name, ending), sepiaImage)
t2 = time.perf_counter()
print("Time used: {}".format(t2-t1))"""
