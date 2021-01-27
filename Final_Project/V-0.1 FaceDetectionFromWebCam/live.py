# This script will detect faces via your webcam.
# Tested with OpenCV3

import requests
import cv2
import numpy as np

url = 'http://192.168.0.101:8080/shot.jpg'

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
	# Capture frame-by-frame
	img_receive = requests.get(url)

	img_arr = np.array(bytearray(img_receive.content), dtype=np.uint8)

	img = cv2.imdecode(img_arr, -1)

	# Our operations on the frame come here
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces)))

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


	# Display the resulting frame
	cv2.imshow('frame', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
