import cv2

facePath = 'face.mp4'
no_facePath = 'no_face.mp4'
count = 0


vc = cv2.VideoCapture(no_facePath)
while vc.isOpened():
	ret, img = vc.read()
	if not ret:
		print("no frame:(")
		break

	count += 1
	img_name = 'no_face_' + str(count) + '.jpg'

	cv2.imwrite(img_name, img)
	cv2.imshow('Output', img)
	print(img_name + '-- saved!!')

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

