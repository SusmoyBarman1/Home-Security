from imutils.video import VideoStream
from imutils
import cv2
import os
import urllib.request
import numpy as np
from django.conf import settings

face_detector = cv2.CascadeClassifier(
	os.path.join(settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml')
)

class IPCamera(object):

	def __init__(self):
		self.url = "http://192.168.0.101:8080/shot.jpg"

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):

		# Getting the image trough api and convert it to actual RGB image
		img_receive = urllib.request.urlopen(self.url)
		image = np.array(bytearray(img_receive.read()), dtype=np.uint8)
		image = cv2.imdecode(image, -1)

		# harcascade give more accurate result in gray image
		grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		faces = face_detector.detectMultiScale(
								grayImage,
								scaleFactor=1.3,
								minNeighbors=5
								)	

		# drawing rectangle in faces
		for (x, y, w, h) in faces:
			cv2.rectangle(image, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255))

## Commeting for no reason