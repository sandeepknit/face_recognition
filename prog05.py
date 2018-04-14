# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

def main():
    
    imgpath = "C:\\Users\\sandeep\\Desktop\\Python-OpenCV3-master\\Python-OpenCV3-master\\Dataset\\house.tif"
    img = cv2.imread(imgpath, 0)
    
    outpath = "C:\\Users\\sandeep\\Desktop\\Python-OpenCV3-master\\Python-OpenCV3-master\\Dataset\\4.2.tiff"
    
    cv2.imshow('Lena', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
    main()