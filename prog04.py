# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

def main():
    
    imgpath = "C:\\Users\\sandeep\\Desktop\\Python-OpenCV3-master\\Python-OpenCV3-master\\Dataset\\4.2.02.tiff"
    img = cv2.imread(imgpath,0)
    
    outpath = "C:\\Users\\sandeep\\Desktop\\Python-OpenCV3-master\\Python-OpenCV3-master\\Output\\4.1.03.jpg"
    
    cv2.imshow('Lena', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')
    
    
    
if __name__ == "__main__":
    main()