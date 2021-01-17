import cv2

img = cv2.imread('face_1.jpg')

imgR = cv2.resize(img, (1200, 720))

cv2.imwrite('face_1r.jpg', imgR)

cv2.imshow('Output', img)
cv2.imshow('OutputR', imgR)

cv2.waitKey(0)