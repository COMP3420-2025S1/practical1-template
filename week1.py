import numpy as np
from matplotlib import pyplot as plt
import cv2

# Exercises related to section 1

def greyscale_rowscolumns(greyscaleimage):
    """Return the image resolution (rows, columns) of a greyscale image
    >>> img = np.array([[   0, 255,   0],  \
                        [ 110, 127, 140]])
    >>> greyscale_rowscolumns(img)
    (2, 3)
    """
    return []

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
    return 0

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

def capture_image(webcam_id=0):

    # Initialize the webcam
    print("Initialising video capture")
    cap = cv2.VideoCapture(webcam_id)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    # Capture a single frame
    print("Capturing frame")
    ret, frame = cap.read()

    # Check if the frame was captured correctly
    if not ret:
        print("Error: Could not read frame.")
        exit()

    # Release the webcam
    print("Releasing webcam")
    cap.release()

    # Convert from BGR to RGB
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
