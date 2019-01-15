# coding:utf-8
import cv2
import os
import sys

'''
make the image more bright
convert BGR to HSV and increase the value of v channel
'''

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

if __name__ == '__main__':
    filename = sys.argv[1] # input image
    img = cv2.imread(filename) #load rgb image
    img = increase_brightness(img)
    cv2.imwrite("image_processed.jpg", img)
