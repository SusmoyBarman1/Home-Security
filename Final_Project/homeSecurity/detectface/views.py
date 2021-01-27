from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .camera import IPCamera

# Create your views here.
def detect(request):
	return render(request, 'detectface/detect.html')

def frame_controller(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def webcam_feed(request):
	return StreamingHttpResponse(
					frame_controller(IPCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame'
					)