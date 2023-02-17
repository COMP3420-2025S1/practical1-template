import numpy as np

import week1_solution as week1;

def test_greyscale_rowscolumns():
    img = np.array([[   0, 255,   0],  
                    [ 110, 127, 140]])
    assert week1.greyscale_rowscolumns(img) == (2, 3)

def test_greyscale_invert():
    img = np.array([[   0, 255,   0], 
                    [  50, 200,  50], 
                    [ 110, 127, 140]])
    target = np.array([[255,   0, 255],
                       [205,  55, 205],
                       [145, 128, 115]])
    np.testing.assert_array_equal(week1.greyscale_invert(img), target)
    
def test_greyscale_highest_luminosity():
    img = np.array([[   0, 250,   0],  
                    [  50, 200,  50],  
                    [ 110, 127, 140]])
    assert week1.greyscale_highest_luminosity(img) == 250

def test_greyscale_blackout():
    img = np.array([[   0, 255,   0],  
                    [  50, 200,  50],  
                    [ 110, 127, 140]])
    target = np.array([[  0,   0,   0],
                       [ 50,   0,  50],
                       [110, 127, 140]])
    np.testing.assert_array_equal(week1.greyscale_blackout(img, 200),
                                  target)

def test_colour_rowscolumns():
    img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]],
                    [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    assert week1.colour_rowscolumns(img) == (2, 3)

def test_remove_red():
    img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]],
                    [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    target = np.array([[[  0,   0,   0],
                        [  0, 255,   0],
                        [  0,   0, 255]],
                       [[  0,   0,   0],
                        [  0, 255, 255],
                        [  0, 127, 127]]])

    np.testing.assert_array_equal(week1.remove_red(img),
                                  target)

def test_to_greyscale():
    img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]],
                    [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    target = np.array([[ 85.,  85.,  85.],
                       [  0., 255., 127.]])

    np.testing.assert_array_equal(week1.to_greyscale(img),
                                  target)

def test_mirror_image():
    img = np.array([[[255,   0,   0], [  0, 255,   0], [  0,   0, 255]],
                    [[  0,   0,   0], [255, 255, 255], [127, 127, 127]]])
    target = np.array([[[  0,   0, 255],
                        [  0, 255,   0],
                        [255,   0,   0]],
                       [[127, 127, 127],
                        [255, 255, 255],
                        [  0,   0,   0]]])
    np.testing.assert_array_equal(week1.mirror_image(img),
                                  target)
