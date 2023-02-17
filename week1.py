import numpy as np
from matplotlib import pyplot as plt

# Exercises related to section 1

def greyscale_rowscolumns(greyscaleimage):
    """Return the image resolution (rows, columns) of a greyscale image
    >>> img = np.array([[   0, 255,   0],  \
                        [ 110, 127, 140]])
    >>> greyscale_rowscolumns(img)
    (2, 3)
    """
    return (2, 3)

def greyscale_invert(greyscaleimage):
    """Return a greyscale image with inverted luminosity
    >>> img = np.array([[   0, 255,   0],  \
                        [  50, 200,  50],  \
                        [ 110, 127, 140]])
    >>> greyscale_invert(img)
    array([[255,   0, 255],
           [205,  55, 205],
           [145, 128, 115]])
    """
    return []

def greyscale_highest_luminosity(greyscaleimage):
    """Return the highest luminosity
    >>> img = np.array([[   0, 250,   0],  \
                        [  50, 200,  50],  \
                        [ 110, 127, 140]])
    >>> greyscale_highest_luminosity(img)
    250
    """
    return 250

def greyscale_blackout(greyscaleimage, threshold):
    """Black out pixels equal or brighter than a set threshold
    >>> img = np.array([[   0, 255,   0],  \
                        [  50, 200,  50],  \
                        [ 110, 127, 140]])
    >>> greyscale_blackout(img, 200)
    array([[  0,   0,   0],
           [ 50,   0,  50],
           [110, 127, 140]])
    """
    return []

# Exercises related to section 2

def colour_rowscolumns(colourimage):
    """Return the image resolution (rows, columns)
    >>> img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]], \
                        [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    >>> colour_rowscolumns(img)
    (2, 3)
    """            
    return []

def remove_red(colourimage):
    """Remove information from the red channel
    >>> img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]], \
                        [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    >>> remove_red(img)
    array([[[  0,   0,   0],
            [  0, 255,   0],
            [  0,   0, 255]],
    <BLANKLINE>
           [[  0,   0,   0],
            [  0, 255, 255],
            [  0, 127, 127]]])
    """
    return []

def to_greyscale(colourimage):
    """Convert from colour to greyscale.
    >>> img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]], \
                        [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    >>> to_greyscale(img)
    array([[ 85.,  85.,  85.],
           [  0., 255., 127.]])
    """
    return []

# Exercises related to section 3

def mirror_image(colourimage):
    """Generate a mirror image
    >>> img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]], \
                        [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    >>> mirror_image(img)
    array([[[  0,   0, 255],
            [  0, 255,   0],
            [255,   0,   0]],
    <BLANKLINE>
           [[127, 127, 127],
            [255, 255, 255],
            [  0,   0,   0]]])   
    """
    return []

if __name__ == "__main__":
    import doctest
    doctest.testmod()
