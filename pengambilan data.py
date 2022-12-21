Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
... import numpy as np
... import csv
... import time
... 
... cap = cv2.VideoCapture(0)
... 
... while True:
...     ret, img = cap.read()
...     for x in range (330,340,1):
...         for y in range (220,260,1):
...             color = img[x,y]
...             color = img[x,y,0]
...             color = img[x,y,1]
...             color = img[x,y,2]
...     print('B G R = ',color)
...     cv2.imshow('Pengambilan Database', img)
... 
...     k = cv2.waitKey(30) & 0xff
...     if k == 27:
...         break
... 
... cap.release()
