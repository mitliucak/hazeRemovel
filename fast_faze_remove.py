# coding : utf-8
import cv2
import numpy as np
import sys

'''
description : implement fast haze removal  in python
reference : https://ieeexplore.ieee.org/document/6561607
'''

def brighten(src_img):
    src_inverse = ~src_img
    hazeRemove_img = fastHazeRemoval(src_inverse)
    dst = ~hazeRemove_img
    return dst

def fastHazeRemoval(img):
    channels = np.shape(img)[2]
    if channels == 1:
        dst = fastHazelRemoval_1channel(img)
    elif channels == 3:
        dst = fastHazelRemoval_3channel(img)
    else:
        dst = img
    return dst

def fastHazelRemoval_1channel(img):
    //TODO
    pass

def fastHazelRemoval_3channel(img):
    beta = 1
    alpha = 1
    # save the origin reverse image
    h_img = img
    # get the min pixel value for each channel
    min_img = h_img.min(2)
    max_img = h_img.max(2)
    # get the mean blur value
    mean_img = cv2.blur(min_img,(80,80))
    # get the toal mean value
    mean_value = np.mean(min_img)/255.0
    # calculate L image
    l_img = np.array([ min(beta*mean_value, 0.9) * mean_img, min_img]).min(0)
    #print np.shape(l_img)
    # calculate A
    a_value = 0.5 * np.max(max_img) + 0.5 * np.max(mean_img)
    # calculate f
    #print np.shape(l_img[:,:,np.newaxis].repeat([3],axis=2))
    a = (1 - l_img / a_value)
    f_img = (h_img - l_img[:,:,np.newaxis].repeat([3],axis=2)) / (1 - l_img / a_value)[:,:,np.newaxis].repeat([3],axis=2)
    return f_img.astype(np.uint8)

    
if __name__ == '__main__':
    filename = sys.argv[0]
    im = cv2.imread(filename)
    im = brighten(im)
    cv2.imwrite('fast_image_process.jpg', im)
