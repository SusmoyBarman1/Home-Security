import cv2

facePath = 'face.mp4'
no_facePath = 'no_face.mp4'
count = 0


vc = cv2.VideoCapture(facePath)
while vc.isOpened():
	ret, img = vc.read()
	if not ret:
		print("no frame:(")
		break

	count += 1
	img_name = 'face_' + str(count) + '.jpg'

	imgR = cv2.resize(img, (1200, 720))

	cv2.imwrite(img_name, imgR)
	cv2.imshow('Output', imgR)
	
	print(img_name + '-- saved!!')

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

