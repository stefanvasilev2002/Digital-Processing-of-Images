import cv2
import numpy as np

image = cv2.imread('img1.jpg', cv2.COLOR_BGR2GRAY)

filter1 = np.array([[-1, -1, -1], [0, 1, 0], [1, 1, 1]])
filter2 = np.array([[1, 0, -1], [1, 1, -1], [1, -1, -1]])
filter3 = np.array([[2, 1, 0], [-1, 1, 1], [1, 1, 1]])
filter4 = np.array([[1, 0, -1], [-1, 1, 1], [1, 1, 1]])

result1 = cv2.filter2D(image, -1, filter1)
result2 = cv2.filter2D(image, -1, filter2)
result3 = cv2.filter2D(image, -1, filter3)
result4 = cv2.filter2D(image, -1, filter4)

combined_result = cv2.bitwise_or(cv2.bitwise_or(result1, result2), cv2.bitwise_or(result3, result4))

cv2.imshow('Filter 1', result1)
cv2.imshow('Filter 2', result2)
cv2.imshow('Filter 3', result3)
cv2.imshow('Filter 4', result4)
cv2.imwrite('Filter_1.jpg', result1)
cv2.imwrite('Filter_2.jpg', result2)
cv2.imwrite('Filter_3.jpg', result3)
cv2.imwrite('Filter_4.jpg', result4)
cv2.imwrite('Combined Result.jpg', combined_result)

cv2.waitKey(0)
