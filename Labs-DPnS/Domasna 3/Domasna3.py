import cv2

img = cv2.imread('Leaves/10000.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Бинаризација на сликата со Otsu thresholding
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Прикажување на бинаризираната слика
cv2.imwrite('binary3.jpg', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Пронаоѓање на контурите на бинаризираната слика
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_copy = img.copy()

# Цртање на контурите во зелена боја
cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 2)

cv2.imwrite('contours3.jpg', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
