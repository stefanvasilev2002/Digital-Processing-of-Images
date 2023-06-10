import cv2 as cv2
import matplotlib.pyplot as mpl

img = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)

img_5 = img[:, :] & 0b11111000
img_4 = img[:, :] & 0b11110000
img_3 = img[:, :] & 0b11100000
img_2 = img[:, :] & 0b11000000
img_1 = img[:, :] & 0b10000000

fig, ax = mpl.subplots(1, 5, figsize=(15, 5))

plotter = ax.flatten()

plotter[0].imshow(img_5, 'gray')
plotter[0].set_title('5 bits')
plotter[0].axis('off')

plotter[1].imshow(img_4, 'gray')
plotter[1].set_title('4 bits')
plotter[1].axis('off')

plotter[2].imshow(img_3, 'gray')
plotter[2].set_title('3 bits')
plotter[2].axis('off')

plotter[3].imshow(img_2, 'gray')
plotter[3].set_title('2 bits')
plotter[3].axis('off')

plotter[4].imshow(img_1, 'gray')
plotter[4].set_title('1 bit')
plotter[4].axis('off')

mpl.show()
cv2.imshow('s', img_3)
cv2.waitKey(0)

