# Image filtering
For information about the InstaPy package, please read the README in the instapy directory.

The programs in this project are used to apply gray or sepia filter to images using either plain Python, Numpy or Numba.

## Requirements
To use the scrips you need to have Python installed. This can be downloaded from the web.\
You need to have Python version 3.7 or higher.\
This can be checked using
```bash
python --version
```
If you have an older Python, you need to update it. How to do this can be found on the web.\
To install the package you need to have pip installed on your computer. This comes automatic when installng Python.\
You also need to have cv2 installed. \
This can be done with
```bash
sudo apt update
sudo apt install python3-opencv
```
To use the tests you need to have pytest installed.\
This can be done with
```bash
pip install pytest
```

## Scrips
All the scrips are placed in seperate files in the instapy folder.\
The scripts can be run using
```bash
python {python/numpy/numba}_color2gray.py
```
or
```bash
python {python/numpy/numba}_color2sepia.py
```
To use the scripts without importing them into another script you will need to uncomment the bottom part of the file and change "rain.jpg" with the filename of the image you want to use the filter on. Remember to have the image in the same directory as the script.\
You can import the scripts into other scripts with
```python
from instapy import {python/numpy/numba}_color2gray.py / {python/numpy/numba}_color2sepia.py
```
This will import the color2gray/color2sepia function from the selected implementation.

## Tests
The tests can be run from the tests directory using
```bash
pytest
```
This test will test all inplmentations of the functions golor2gray and color2sepia.
