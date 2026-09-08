import os
import cv2 as cv
import numpy as np

def videoFromWebcam():
    cap = cv.VideoCapture(0)


    # if video camera already in use, exit program
    if not cap.isOpened():
        exit()

    # while loop to keep getting video frames from webcam
    # while true, return frame by reading the cap variable with the videCapture object

    while True:
        # ret is a boolean variable that returns true if the frame is available
        # frame is a numpy array that contains the height, 
        # width and colr channel image data of each frame
        ret, frame = cap.read()

        #if it returned true, show frame with frame name from frame
        if ret:
            cv.imshow('WebCam Video', frame)

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


def videoFromFile():
    root = os.getcwd()
    vidPath = os.path.join(root, '.\\storage\\videos\\oreospin.mp4')
    vidCap = cv.VideoCapture(vidPath)

    while vidCap.isOpened():
        ret, frame = vidCap.read()
        cv.imshow('Video from file', frame)
        delay = int(1000/60)
        if cv.waitKey(delay) == ord('q'):
            break




if __name__ == '__main__':
    videoFromFile()