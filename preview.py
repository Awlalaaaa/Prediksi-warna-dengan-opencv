Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>  import cv2
... import numpy as np
... cap = cv2.VideoCapture (1)
... while True:
...     ret, frame = cap.read()
...     frame = cv2.flip (frame,1)
...     cv2.imshow("camera", frame)
...     key = cv2.waitKey (1)
...     if key == 27:
...             break
... cap.release()
