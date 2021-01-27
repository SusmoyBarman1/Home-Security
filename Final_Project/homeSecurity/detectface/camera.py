from imutils.video import VideoStream
import imutils
import cv2
import os
import urllib.request
import numpy as np
from django.conf import settings

face_detector = cv2.CascadeClassifier(
	os.path.join(settings.BASE_DIR,'data/opencv_haarcascade_data/haarcascade_frontalface_default.xml')
)

class IPCamera(object):

	def __init__(self):
		self.url = "http://192.168.0.100:8080/shot.jpg"

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):

		imgReceive = urllib.request.urlopen(self.url)
		imgNp = np.array(bytearray(imgReceive.read()),dtype=np.uint8)
		img= cv2.imdecode(imgNp,-1)

		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream

		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		for (x, y, w, h) in faces:
			cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)

		resizeImage = cv2.resize(img, (640, 480), interpolation = cv2.INTER_LINEAR) 
		frame_flip = cv2.flip(resizeImage, 1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		
		return jpeg.tobytes()