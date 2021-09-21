import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instapy",
    version="0.0.1",
    author="Patrick P. Haukaa",
    author_email="patricph@uio.no",
    description="Instagram filters in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.uio.no/IN3110/IN3110-patricph/tree/master/assignment4",
    packages=setuptools.find_packages(),
    scripts=["bin/instapy"],
    setup_requires=["numpy", "setuptools>=18.0"],
    install_requires=["numpy", "numba", "opencv-python"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
