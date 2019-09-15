import numpy as np
import cv2
import matplotlib.pyplot as plt

bandeira = cv2.imread('bandeira_brasil.jpeg')

cv2.imshow('bandeira', bandeira)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('passou')