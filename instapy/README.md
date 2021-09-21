# InstaPy

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install instapy
```bash
pip install .
```

## Usage
To use the package, use the following command
```bash
instapy {flags}
```
### Available flags:
Required:
```bash
-f {FILENAME} #Filename of the file you want to apply filter to
-g or -se #-g for grayscale, -se for sepia filter
```
Other:
```bash
-h #Help flag
-sc #To resize the image to a scale
-i #To use a specific implementation of the filters
-o {FILENAME} #Output filename of the image with filter applied
```