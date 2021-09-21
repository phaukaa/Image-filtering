import cv2
import time
import numpy as np

def color2sepia(image, sepiagrade=1):
    """
    Function to turn image into sepia using numpy
    param1 (numpy.ndarray): image
    param2 (optional) (float): the grade of which you want to apply sepia filter
                                100% = 1, 0% = 0
                                default: 1
    return (numpy.ndarray): grayscaleimage (ndarray)
    """
    sepiamatrix = np.array([[0.393 + 0.607 * (1 - sepiagrade), 
                    0.769 - 0.769 * (1 - sepiagrade), 
                    0.189 - 0.189 * (1 - sepiagrade)],
                   [0.349 - 0.349 * (1 - sepiagrade), 
                    0.686 + 0.314 * (1 - sepiagrade), 
                    0.168 - 0.168 * (1 - sepiagrade)],
                   [0.272 - 0.349 * (1 - sepiagrade), 
                    0.534 - 0.534 * (1 - sepiagrade), 
                    0.131 + 0.869 * (1 - sepiagrade)]])

    bgrMatrix = sepiamatrix[::-1]

    sepiaimage = image.dot(bgrMatrix.T)
    sepiaimage[np.where(sepiaimage > 255)] = 255
    
    return sepiaimage

"""t1 = time.perf_counter()
filename = "rain.jpg"
image = cv2.imread(filename)
sepiaimage = color2sepia(image)
name = filename.split(".")[0]
ending = filename.split(".")[1]
sepiaimage = sepiaimage.astype("uint8")
cv2.imwrite("{}_sepia.{}".format(name, ending), sepiaimage)
t2 = time.perf_counter()
print("Time used: {}".format(t2-t1))"""
