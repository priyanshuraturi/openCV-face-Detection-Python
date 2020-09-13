#!/usr/bin/python
import cv2
import os
import sys
def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images
if __name__ == '__main__':
    if len(sys.argv) == 3:
        path1 = sys.argv[1]
        path2 = sys.argv[2]
    else:
        print("Failed To Provide Correct Arguments \n imgext.py path_of_diectory path_of_result_directory")
        sys.exit(0)

    path = path2
    count = 0
    face_cascade = cv2.CascadeClassifier('face_detector.xml')
    for image in load_images(path1):
        imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(imgGray, scaleFactor=1.2, minNeighbors=5);
        if len(face_rects > 0):
            count = count + 1
            path = path + "img" + str(count) + ".jpg"
            cv2.imwrite("path", image)
