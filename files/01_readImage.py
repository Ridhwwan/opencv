import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

# read an image
def readImage():
    root = os.getcwd()
    imgPath = os.path.join(root,'..\\storage\\images\\lampbg.png')
    img = cv.imread(imgPath)
    debug = 1
    cv.imshow ('img', img)
    cv.waitKey(0) 
    # 0 is a delay time in milliseconds. 0 means wait indefinitely until a key is pressed


# write an image
def writeImage():
    root = os.getcwd()
    imgPath = os.path.join(root,'.\\storage\\images\\lampbg.png')
    img = cv.imread(imgPath)
    outPath = os.path.join(root,'.\\storage\\images\\lampbgoutput.png')

    # if image with the same name exists, it will be overwritten
    cv.imwrite(outPath, img)




    
if __name__ == '__main__':
    # readImage()
    writeImage()