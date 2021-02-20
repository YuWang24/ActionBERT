import cv2
import os


def video_converter(path):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(subdir, file)
            name = file_path.split('\\')[1][:-4] + 'avi'
            print(file_path[:-4] + 'avi')
            img = cv2.imread(file_path)
            height, width, layers = img.shape
            size = (width, height)
            out = cv2.VideoWriter(file_path[:-4] + 'avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
            out.write(img)
    return


path = 'C:/Users/Yu/Desktop/Study/DefenceProject/ActionBERT-master/fine_grained_objects/'
video_converter(path)
