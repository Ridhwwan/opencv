import os
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv



def writeImage():
# store current working directory in variable named root
    root = os.getcwd()
    mergeRoot = os.path.join(root, '.\\storage\\images\\lampbg.png')

    # read image from merged directories
    img = cv.imread(mergeRoot)

    # merge root variable with the output directory for the write image
    writingPath = os.path.join(root, '.\\storage\\images\\savedImage.png')
    cv.imwrite(writingPath, img)



if __name__ == '__main__':
    writeImage()