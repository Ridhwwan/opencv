import os 
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt





def readImage():
    # get the current work directory from os and store it in the root variable
    root = os.getcwd()

    # get the local image path and join it with the root directory os.path.join
    getImagPath = os.path.join(root, '.\\storage\\images\\lampbg.png')

    # use cv to read the merged image path and store it in the variable called img
    img = cv.imread(getImagPath)

    # create a window title variable to store input from the user
    windowTitle = input('Enter your window title here: ')

    # display the image from the img variable. first argument is window 
    # title as a formatted variable, second argument is the read image variable.
    cv.imshow(f'{windowTitle}', img)

    # wait for a key press to close the opened windows. 0 means it'll wait indefinitely until a key is pressed
    cv.waitKey(0)



if __name__ == '__main__':
    readImage() 
